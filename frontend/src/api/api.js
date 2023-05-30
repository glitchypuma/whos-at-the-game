import dev from './test';
import prod from './prod';

// MOCK DATA
// export default process.env.NODE_ENV === 'production' ? prod : dev;

// PROD DATA
export default process.env.NODE_ENV === 'development' ? prod : dev;