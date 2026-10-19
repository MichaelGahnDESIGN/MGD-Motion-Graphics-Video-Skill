/* Bewegungen liegen in einer pausierten Timeline. Die Lesedauer beginnt erst,
   wenn die Schlusskarte vollständig eingeblendet und zur Ruhe gekommen ist. */
(() => {
  const c = window.MGD_CONFIG;
  const tl = gsap.timeline({ paused: true });
  gsap.set('#middle, #final', { opacity: 0 });
  tl.fromTo('#intro', { opacity: 0, y: 55, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.8, ease: 'power3.out' }, 0);
  tl.to('#intro', { opacity: 0, y: -60, duration: 0.45, ease: 'power2.in' }, c.intro_duration - 0.45);
  tl.fromTo('#middle', { opacity: 0, y: 80, scale: 1.08 }, { opacity: 1, y: 0, scale: 1, duration: 0.65, ease: 'power3.out' }, c.intro_duration - 0.15);
  tl.to('#middle', { opacity: 0, y: -45, duration: 0.45 }, c.end_start - 0.45);
  tl.fromTo('#final', { opacity: 0, y: 50, scale: 0.96 }, { opacity: 1, y: 0, scale: 1, duration: c.end_entrance, ease: 'power3.out' }, c.end_start);
  tl.to('#final', { opacity: 0, duration: c.end_fade }, c.readable_from + c.end_hold);
  tl.fromTo('#world', { scale: 1.03, x: -12 }, { scale: 1.15, x: 12, duration: c.duration, ease: 'none' }, 0);
  tl.fromTo('#mountains-near', { y: 25 }, { y: -65, duration: c.duration, ease: 'none' }, 0);
  tl.fromTo('#mist', { x: -60 }, { x: 80, duration: c.duration, ease: 'none' }, 0);
  window.mgdParticles(tl, c);
  window.__timelines = window.__timelines || {};
  window.__timelines.main = tl;
})();
