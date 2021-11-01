import React from 'react';
function App() {
  return (
    <div className="container">
      <div className="center col">
          <h1>Baby Cam</h1>
          <img src="/video" className="video-feed"/>
          <a href="/cam" className="btn">On/Off</a>
      </div>
    </div>
  );
}

export default App;
