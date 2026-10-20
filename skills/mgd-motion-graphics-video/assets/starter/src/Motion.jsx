import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const ease = (x) => 1 - Math.pow(1 - Math.max(0, Math.min(1, x)), 3);

// Jede Eigenschaft folgt dem Frame. Vor- und Rückwärtssprünge liefern dasselbe Bild.
// Keine Echtzeituhr, zufälligen Zustände, Webfonts oder externen Bildquellen.
export const Motion = ({config: c}) => {
  const frame = useCurrentFrame();
  const t = frame / c.fps;
  const wide = c.width > c.height;
  const phase = t < c.intro_duration ? 0 : t < c.end_start ? 1 : 2;
  const start = [0, c.intro_duration, c.end_start][phase];
  const enter = ease((t-start) / (phase === 2 ? c.end_entrance : 0.75));
  const fade = interpolate(t, [c.duration-c.end_fade, c.duration], [1,0], clamp);
  const title = [c.headline,c.message,c.brand][phase];
  const words = title.trim().split(/\s+/);
  const lines = wide ? [title] : [words.slice(0,Math.ceil(words.length/2)).join(' '),words.slice(Math.ceil(words.length/2)).join(' ')].filter(Boolean);
  const longest = Math.max(...lines.map(s => s.length), 1);
  const fontSize = Math.min(wide ? 105 : 100, 840 / (longest * 0.66));
  return <AbsoluteFill style={{background:'#090f25',color:'#f6eee1',fontFamily:'serif',opacity:fade}}>
    <svg viewBox="0 0 1080 1920" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" style={{position:'absolute'}}>
      <defs>
        <radialGradient id="light"><stop stopColor="#395d84"/><stop offset="1" stopColor="#090f25"/></radialGradient>
        <linearGradient id="mountain" x2="0" y2="1"><stop stopColor="#2a435f"/><stop offset="1" stopColor="#11182d"/></linearGradient>
        <radialGradient id="spark"><stop stopColor="#fff4cc"/><stop offset="0.3" stopColor="#e8bd6f" stopOpacity=".8"/><stop offset="1" stopColor="#e8bd6f" stopOpacity="0"/></radialGradient>
      </defs>
      <rect width="1080" height="1920" fill="url(#light)"/>
      <circle cx={700+Math.sin(t*.16)*30} cy="470" r="175" fill="#e9c985" opacity=".07"/>
      {[0,1,2].map(layer => <path key={layer} d="M-200 1500 L100 780 L310 1150 L540 660 L790 1100 L1030 770 L1280 1400 V2200 H-200Z"
        fill={layer === 0 ? 'url(#mountain)' : ['','#142239','#0d1529'][layer]}
        transform={`translate(${Math.sin(t*.18+layer)*18*(layer+1)},${layer*175}) scale(${1+t*.002})`} />)}
      {Array.from({length:64},(_,i) => {
        const x=(i*173.17+Math.sin(t*.45+i)*18)%1080;
        const y=((i*229.31-t*(10+i%7))+3840)%1920;
        const r=5+(i%4)*2;
        return <circle key={i} cx={x} cy={y} r={r} fill="url(#spark)" opacity={.3+.55*(.5+.5*Math.sin(t*.9+i))}/>;
      })}
    </svg>
    <AbsoluteFill style={{justifyContent:'center',alignItems:'center',padding:wide?'7%':'10%',background:'linear-gradient(transparent, #090f2533 50%, #090f25aa)'}}>
      <div style={{width:'100%',textAlign:'center',transform:`translateY(${(1-enter)*70}px) scale(${.94+enter*.06})`,opacity:enter}}>
        <div style={{fontFamily:'sans-serif',fontSize:wide?22:26,letterSpacing:5,color:'#dfbc78',marginBottom:40}}>MOTION · DESIGN · EMOTION</div>
        <div style={{fontSize:fontSize*c.width/1080,lineHeight:1.16,fontWeight:600,textShadow:'0 3px 30px #0008'}}>
          {lines.map((line,i)=><div key={i}>{line}</div>)}
        </div>
        {phase === 2 && <div style={{fontSize:(wide?32:38)*c.width/1080,marginTop:45,color:'#dfbc78'}}>{c.tagline}</div>}
      </div>
    </AbsoluteFill>
  </AbsoluteFill>;
};
