## Hosted on AWS Amplify

Since Amazon Linux:2 (default) does not support Node 18.16.0, we use the custom image `nikolaik/python-nodejs:python3.11-nodejs18` provided by [nikolaik/python-nodejs](https://hub.docker.com/r/nikolaik/python-nodejs/). Merges to `main` are automatically deployed to production.

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