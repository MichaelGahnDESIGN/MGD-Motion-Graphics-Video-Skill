/** Lokales Remotion-Rendering mit ausdrücklich vorhandenem Browser.
 * Installation und Browserdownload gehören nicht zu einem Prüf-/Renderaufruf.
 * Arbeitsdateien bleiben im Auftragsordner; die Python-Hülle schützt Exporte.
 */
import path from 'node:path';
import fs from 'node:fs';
import {bundle} from '@remotion/bundler';
import {getCompositions, renderStill, renderMedia} from '@remotion/renderer';

const [action, work, browser, ...times] = process.argv.slice(2);
if (!['check','snapshot','render'].includes(action) || !work || !fs.existsSync(browser)) {
  throw new Error('Aktion, Arbeitsordner und vorhandener Browser erforderlich');
}
const root = process.cwd();
const serveUrl = await bundle({entryPoint:path.join(root,'src/index.jsx'),
  outDir:path.join(work,'bundle'), webpackOverride:(config)=>({...config,cache:false})});
const errors=[];
const onBrowserLog=(log)=>{if(log.type==='error') errors.push(log.text);};
const options={serveUrl,browserExecutable:browser,onBrowserLog};
const compositions=await getCompositions(serveUrl,{browserExecutable:browser,onBrowserLog});
const composition=compositions.find(c=>c.id==='main');
if(!composition) throw new Error('Komposition main fehlt');
if(action==='snapshot') {
  for(let i=0;i<times.length;i++) {
    const frame=Math.round(Number(times[i])*composition.fps);
    if(!Number.isFinite(frame) || frame<0 || frame>=composition.durationInFrames) throw new Error('Snapshot außerhalb der Timeline');
    await renderStill({...options,composition,frame,output:path.join(work,`snapshot-${i}-${frame}.png`)});
  }
}
if(action==='render') {
  await renderMedia({...options,composition,codec:'h264',crf:15,pixelFormat:'yuv420p',
    imageFormat:'png',colorSpace:'bt709',concurrency:2,outputLocation:path.join(work,'export.mp4')});
}
if(errors.length) throw new Error(errors.join('\n'));
console.log(JSON.stringify({action,composition,work,browserErrors:errors},null,2));
