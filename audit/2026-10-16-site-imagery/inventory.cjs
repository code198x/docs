const fs=require('node:fs'),path=require('node:path');
if (!process.argv[2]) throw new Error('Pass the website checkout path');
const base=path.resolve(process.argv[2]);
const revision=require('node:child_process').execFileSync('git',['-c','core.fsmonitor=false','rev-parse','HEAD'],{cwd:base,encoding:'utf8'}).trim();
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)]);
const rows=walk(base+'/src/content').filter(f=>/\.mdx?$/.test(f)).map(f=>{
 const text=fs.readFileSync(f,'utf8');const body=text.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/,'');
 const noCode=body.replace(/^```[^\n]*\n[\s\S]*?^```\s*$/gm,'');
 const raster=[...noCode.matchAll(/!\[[^\]]*\]\([^\n)]+\)|<(?:img|Image|Picture|NativeImage)\b/g)].length;
 const inline=[...noCode.matchAll(/<(?:svg|canvas)\b/g)].length;
 const components=[...new Set([...noCode.matchAll(/<([A-Z][A-Za-z0-9]+)\b/g)].map(m=>m[1]))].sort();
 return {path:path.relative(base,f),collection:path.relative(base+'/src/content',f).split('/')[0],rasterMarkers:raster,inlineVisualMarkers:inline,mermaidBlocks:(body.match(/^```mermaid\b/gm)||[]).length,components};
});
const stats=[...new Set(rows.map(r=>r.collection))].sort().map(c=>{const r=rows.filter(x=>x.collection===c);return {collection:c,files:r.length,withImageMarkers:r.filter(x=>x.rasterMarkers).length,withFigureComponent:r.filter(x=>x.components.includes('Figure')).length,withImageOrFigureMarkers:r.filter(x=>x.rasterMarkers||x.components.includes('Figure')).length,withInlineSvgCanvas:r.filter(x=>x.inlineVisualMarkers).length,withMermaid:r.filter(x=>x.mermaidBlocks).length,components:[...new Set(r.flatMap(x=>x.components))].sort()}});
fs.writeFileSync(__dirname+'/content-inventory.json',JSON.stringify({sourceRevision:revision,method:'Literal media markers outside fenced code. Component references listed separately, not expanded. Counts are source files, not rendered pages or quality measures.',stats,rows},null,2));
console.log(JSON.stringify(stats,null,2));
