import React from 'react';
import ReactDOM from 'react-dom';


const App = () => (
  <div>
    <h1>Coming soon</h1>
    <p>In the meantime, here&rsquo;s a free <a href="/api/">BJCP API</a></p>
    <p>Foaming beergreets,<br />
    -Bj&ouml;rn
    </p>
  </div>
);


ReactDOM.render(
  <App />,
  document.getElementById('app'),
);
