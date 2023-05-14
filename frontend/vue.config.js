const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  //https://cli.vuejs.org/config/#devserver
  devServer: {
    proxy:  {
      '/api': {
        target: 'http://localhost:8000'
      },
    }
  }
})
