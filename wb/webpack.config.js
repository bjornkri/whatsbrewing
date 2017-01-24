module.exports = {
  context: __dirname + '/js_src',
  entry: './app.jsx',
  output: {
    filename: 'app.js',
    path: __dirname + '/static/js/',
  },
  resolve: {
    extensions: ['', '.js', '.jsx', '.json'],
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loaders: ['babel-loader'],
      },
    ],
  },
};
