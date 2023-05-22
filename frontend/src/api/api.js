import dev from './test/games';
import prod from './prod/games';

// MOCK DATA
// export default process.env.NODE_ENV === 'production' ? prod : dev;

// PROD DATA
export default process.env.NODE_ENV === 'development' ? prod : dev;