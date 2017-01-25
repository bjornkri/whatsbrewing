import React from 'react';
import ReactDOM from 'react-dom';
import '../scss/app.scss';


const App = () => (
  <div>
    <h2>Coming soon</h2>
    <p>In the meantime, here&rsquo;s a free <a href="/api/">BJCP API</a></p>
    <p>Beergreets,<br />
    -Bj&ouml;rn
    </p>
  </div>
);


ReactDOM.render(
  <App />,
  document.getElementById('app'),
);
