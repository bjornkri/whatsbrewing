import React from 'react';
import ReactDOM from 'react-dom';
import '../scss/app.scss';


const Footer = () => (
  <p>Beergreets,<br />
  -Bj&ouml;rn
  </p>
);

const App = () => (
  <div>
    <h1>What&rsquo;s Brewing?</h1>
    <h2>Coming soon</h2>
    <p>In the meantime, here&rsquo;s a free <a href="/api/">BJCP API</a></p>
    <Footer />
  </div>
);


ReactDOM.render(
  <App />,
  document.getElementById('app'),
);
