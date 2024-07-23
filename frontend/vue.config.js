const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  chainWebpack: config => {
    config.plugin('html')
      .tap(args => {
        args[0].title = process.env.APP_NAME;
        args[0].favicon = './public/favicon.ico';
        args[0].meta = {
          ...args[0].meta,
          'og:title': process.env.APP_NAME,
          'og:description': process.env.APP_DESC,
          'og:image': '../public/favicon.ico',
          'og:type': 'website',
          'og:site_name': 'My Site'
        };
        return args;
      });
  },
  transpileDependencies: [
    'vuetify'
  ]
})
