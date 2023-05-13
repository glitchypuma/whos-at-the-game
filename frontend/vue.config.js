const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      'ws://192.168.1.7:8080/ws': {
        target: 'https://localhost:8080',
        secure: false,
        changeOrigin: true,
        // pathRewrite: {
        //   '^/api': '/api'
        // }, 
        logLevel: 'debug',
        headers: { 
          Connection: 'keep-alive'
       },
      }
     }
  }
})
