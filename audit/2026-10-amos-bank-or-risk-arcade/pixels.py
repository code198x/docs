"""Read the emulator's unedited 8-bit RGB/RGBA PNGs without image dependencies."""

from __future__ import annotations

import struct
import zlib
from pathlib import Path


def read_png(path: Path) -> tuple[int, int, bytes]:
    data = path.read_bytes()
    assert data.startswith(b"\x89PNG\r\n\x1a\n")
    offset = 8
    compressed = bytearray()
    width = height = channels = 0
    while offset < len(data):
        size = int.from_bytes(data[offset : offset + 4], "big")
        kind = data[offset + 4 : offset + 8]
        payload = data[offset + 8 : offset + 8 + size]
        crc = int.from_bytes(data[offset + 8 + size : offset + 12 + size], "big")
        assert zlib.crc32(kind + payload) & 0xFFFFFFFF == crc, path.name
        if kind == b"IHDR":
            width, height, depth, colour, compression, filtering, interlace = (
                struct.unpack(">IIBBBBB", payload)
            )
            assert (
                depth == 8
                and colour in (2, 6)
                and compression == filtering == interlace == 0
            )
            channels = 3 if colour == 2 else 4
        if kind == b"IDAT":
            compressed.extend(payload)
        offset += size + 12
    assert width > 0 and height > 0 and channels
    raw = zlib.decompress(compressed)
    stride = width * channels
    assert len(raw) == height * (stride + 1)
    decoded = bytearray()
    previous = bytes(stride)
    for y in range(height):
        start = y * (stride + 1)
        kind = raw[start]
        row = bytearray(raw[start + 1 : start + 1 + stride])
        assert 0 <= kind <= 4
        for i in range(stride):
            left = row[i - channels] if i >= channels else 0
            up = previous[i]
            corner = previous[i - channels] if i >= channels else 0
            if kind == 1:
                predict = left
            elif kind == 2:
                predict = up
            elif kind == 3:
                predict = (left + up) // 2
            elif kind == 4:
                estimate = left + up - corner
                distances = [
                    abs(estimate - left),
                    abs(estimate - up),
                    abs(estimate - corner),
                ]
                predict = [left, up, corner][distances.index(min(distances))]
            else:
                predict = 0
            row[i] = (row[i] + predict) & 255
        if channels == 4:
            assert all(row[i] == 255 for i in range(3, stride, 4))
        decoded.extend(
            value for i, value in enumerate(row) if channels == 3 or i % 4 != 3
        )
        previous = row
    return width, height, bytes(decoded)


def colours(path: Path) -> set[tuple[int, int, int]]:
    _, _, pixels = read_png(path)
    return set(zip(pixels[::3], pixels[1::3], pixels[2::3], strict=True))
