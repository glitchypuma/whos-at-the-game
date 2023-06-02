import dev from './test';
import prod from './prod';

export default process.env.NODE_ENV === 'production' ? prod : dev;