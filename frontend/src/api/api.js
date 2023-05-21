// const prod = require('./prod');
// const dev = require('./test/games');

// module.exports = process.env.NODE_ENV === 'production' ? dev : prod;
import dev from './test/games';
import prod from './prod/games';

export default process.env.NODE_ENV === 'production' ? prod : dev;
// export default process.env.NODE_ENV === 'development' ? prod : dev;