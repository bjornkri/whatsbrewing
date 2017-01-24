import React from 'react';
import ReactDOM from 'react-dom';


class App extends React.Component {
  render () {
    return (
      <div>
        <h1>Coming soon</h1>
        <p>In the meantime, here's a free <a href="/api/">BJCP API</a></p>
      </div>
    )
  }
}


ReactDOM.render(
  <App />,
  document.getElementById('app')
);
