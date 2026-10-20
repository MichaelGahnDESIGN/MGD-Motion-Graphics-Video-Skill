import React from 'react';
import {Composition} from 'remotion';
import config from '../runtime-config.json';
import {Motion} from './Motion';

// Export und Komposition beziehen ihre Werte aus derselben geprüften Zeitplanung.
export const Root = () => <Composition id="main" component={Motion}
  width={config.width} height={config.height} fps={config.fps}
  durationInFrames={config.frames} defaultProps={{config}} />;
