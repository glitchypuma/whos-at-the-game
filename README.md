# Who's at the Game?
(WIP) Website that uses Twitter API to make an educated guess about what celebrities are attending today's sports games

## APIs

* [api-basketball](https://www.api-basketball.com/) Basic/Free Plan
    * At 100 requests/day, we can limit our requests by requesting each days' games once and storing the data... we don't need any updates after that.
* [statsapi.mlb](https://statsapi.mlb.com/docs/login?referrerUrl=https://statsapi.mlb.com/docs/)
    * I'm not sure... maybe this is just for pitching/hitting/etc stats and not basic game info... in which case we should look at [api-baseball](https://api-sports.io/documentation/baseball/v1)

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).