const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  //https://cli.vuejs.org/config/#devserver
  devServer: {
    proxy:  {
      '/baseball_games': {
        target: 'http://localhost:8000'
      },
    }
  }
})
