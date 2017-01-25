module.exports = {
  context: __dirname + '/app/js',
  entry: './app.jsx',
  output: {
    filename: 'app.js',
    path: __dirname + '/static/js/',
  },
  resolve: {
    extensions: ['', '.js', '.jsx', '.json'],
  },
  devtool: 'source-map',
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loaders: ['babel-loader'],
      },
      {
        test: /\.scss$/,
        loaders: ['style-loader', 'css-loader?sourceMap', 'sass-loader?sourceMap'],
      },
    ],
  },
};
