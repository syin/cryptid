const path = require('path')
const webpack = require('webpack')

module.exports = {
  entry: {
    index: './static/src/js/main.js',
    lib: './static/src/js/cryptidlib.js'
  },
  mode: 'development',
  output: {
    path: path.resolve(__dirname, 'static/dist'),
    publicPath: './static/dist',
    filename: '[name].bundle.js'
  },
  devtool: 'inline',
  module: {
    rules: [
      {
        test: /\.riot$/,
        exclude: /node_modules/,
        use: [
          {
            loader: '@riotjs/webpack-loader',
            options: {
              hot: true
            }
          }
        ]
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      },
      {
        test: /\.s[ac]ss$/i,
        use: ['style-loader', 'css-loader', 'sass-loader']
      }
    ]
  }
}
