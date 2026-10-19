/* Ein fester Seed macht Lichtpunkte beim beliebigen Anspringen reproduzierbar.
   Die Punkte sind runde Lichtkerne; gestrichelte Kurven werden nicht verwendet. */
window.mgdParticles = function (timeline, config) {
  let seed = 4519;
  const random = () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296; };
  const container = document.querySelector('#particles');
  for (let i = 0; i < 42; i++) {
    const mote = document.createElement('i');
    const size = 6 + random() * 16;
    mote.className = 'mote';
    Object.assign(mote.style, { left: `${random() * 100}%`, top: `${random() * 100}%`, width: `${size}px`, height: `${size}px` });
    container.appendChild(mote);
    timeline.fromTo(mote, { y: 70, x: 0, opacity: 0.12 + random() * 0.45 },
      { y: -170 - random() * 160, x: (random() - 0.5) * 100, duration: config.duration, ease: 'none' }, 0);
  }
};
