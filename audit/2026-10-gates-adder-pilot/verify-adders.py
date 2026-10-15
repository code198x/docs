"""Compare executed Z80 addition with independently reconstructed Boolean adders."""
import argparse
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ripple(a: int, b: int, width: int) -> tuple[int, int, list[dict]]:
    carry, result, trace = 0, 0, []
    for bit in range(width):
        x, y = (a >> bit) & 1, (b >> bit) & 1
        intermediate = x ^ y
        output = intermediate ^ carry
        next_carry = (x & y) | (intermediate & carry)
        trace.append({'bit': bit, 'a': x, 'b': y, 'cin': carry, 'sum': output, 'cout': next_carry})
        result |= output << bit
        carry = next_carry
    return result, carry, trace


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ['samples', 'emulator', 'assembler', 'output']:
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    driver = args.samples / 'sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py'
    spec = importlib.util.spec_from_file_location('completion', driver)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load maintained transport')
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    cases = []
    for a in range(2):
        for b in range(2):
            cases.append({'group': 'half', 'a': a, 'b': b, 'cin': 0, 'width': 1})
            for cin in range(2):
                cases.append({'group': 'full', 'a': a, 'b': b, 'cin': cin, 'width': 1})
    cases += [{'group': 'ripple', 'a': a, 'b': b, 'cin': 0, 'width': 3} for a in range(8) for b in range(8)]
    cases += [{'group': 'byte', 'a': a, 'b': b, 'cin': cin, 'width': 8} for a, b, cin in [(5, 251, 0), (255, 0, 1), (127, 1, 0), (255, 255, 1)]]
    report = {'status': 'running', 'cases': []}

    def read(address: int, size: int) -> bytes:
        result = bytes(machine.call('memory_read', addr=address, len=size)['bytes'])
        if len(result) != size:
            raise AssertionError('Incomplete memory read')
        return result

    try:
        lines = ['; Audit-only arithmetic observations, not a physical gate implementation.', 'org 32768', 'start:', 'di']
        for i, case in enumerate(cases):
            a, b, cin, width = (case[key] for key in ['a', 'b', 'cin', 'width'])
            address = 0xa000 + i * 2
            lines.append(f'ld a,{a}')
            if case['group'] in ['full', 'byte']:
                lines += ['scf' if cin else 'or a', f'adc a,{b}']
            else:
                lines.append(f'add a,{b}')
            if width == 8:
                lines += [f'ld ({address}),a', 'ld a,0', 'adc a,0', f'ld ({address + 1}),a']
            else:
                lines += ['ld e,a', f'and {(1 << width) - 1}', f'ld ({address}),a', 'ld a,e']
                lines += ['srl a'] * width
                lines.append(f'ld ({address + 1}),a')
        lines += ['ld a,165', 'ld ($b100),a', 'hold:', 'jr hold', 'end start']
        source = out / 'adder-cases.asm'
        source.write_text('\n'.join(lines) + '\n')
        binary, tape = out / 'adder-cases.bin', out / 'adder-cases.tap'
        for target, options in [(binary, []), (tape, ['--tapbas'])]:
            subprocess.run([str(args.assembler), '--dialect', 'pasmo', '--cpu', 'z80', *options, str(source), '-o', str(target)], check=True)
        machine.call('load_media', slot='tape-1', kind='tape', path=str(tape))
        machine.statement('LOAD ""')
        machine.call('media_transport', slot='tape-1', transport='start')
        machine.frames(7000)
        code = binary.read_bytes()
        if not 0 < len(code) < 8192:
            raise AssertionError('Unexpected fixture size')
        loaded = b''.join(read(32768 + i, min(256, len(code) - i)) for i in range(0, len(code), 256))
        if loaded != code or read(0xb100, 1) != b'\xa5':
            raise AssertionError('Fixture differs or did not complete')
        data = read(0xa000, len(cases) * 2)
        for i, case in enumerate(cases):
            a, b, cin, width = (case[key] for key in ['a', 'b', 'cin', 'width'])
            low, carry = data[i * 2:i * 2 + 2]
            total = a + b + cin
            if low != total % (1 << width) or carry != total // (1 << width):
                raise AssertionError((case, low, carry))
            if low + (carry << width) != total:
                raise AssertionError('Reconstruction differs')
            if case['group'] == 'ripple':
                model_low, model_carry, trace = ripple(a, b, width)
                if (model_low, model_carry) != (low, carry):
                    raise AssertionError('Boolean ripple and CPU arithmetic disagree')
                case['trace'] = trace
            if case['group'] in ['half', 'full']:
                model_sum = a ^ b ^ cin
                model_carry = (a & b) | ((a ^ b) & cin)
                if (model_sum, model_carry) != (low, carry):
                    raise AssertionError('One-bit Boolean model differs')
            report['cases'].append({**case, 'actual_low': low, 'actual_carry': carry, 'full_result': total})
        if len(report['cases']) != 80:
            raise AssertionError('Missing cases')
        rom = b''.join(read(address, 256) for address in range(0, 16384, 256))
        report.update(status='passed', emulator=machine.server['serverInfo'], emulator_sha256=sha(args.emulator), assembler_sha256=sha(args.assembler), driver_sha256=sha(driver), verifier_sha256=sha(Path(__file__)), rom_sha256=hashlib.sha256(rom).hexdigest(), fixture_sha256=sha(source), code_sha256=sha(binary), tape_sha256=sha(tape), code_bytes=len(code), tape_bytes=tape.stat().st_size, result_bytes=len(data), completion_marker=165, limits='Configured Z80 arithmetic observations and an independent Boolean ripple model. This does not establish the processor gate layout, transistor count, electrical behaviour, propagation time or learner understanding.')
        print('PASS: four half-adder cases, eight full-adder cases, all 64 three-bit pairs and four byte carry cases')
    except BaseException as error:
        report.update(status='failed', failure=repr(error))
        raise
    finally:
        (out / 'native-adders.json').write_text(json.dumps(report, indent=2) + '\n')
        machine.close()


if __name__ == '__main__':
    main()
