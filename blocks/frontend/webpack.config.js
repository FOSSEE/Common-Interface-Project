var HtmlWebpackPlugin = require('html-webpack-plugin');

plugins = [
    new HtmlWebpackPlugin({
        favicon: "./src/favicon.ico"
    })
];

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};
