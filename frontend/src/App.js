import React from 'react';
import Navbar from './components/Navbar';
import Introduction from './components/Introduction';
import Detector from './components/Detector';
import './App.css';

function App() {
  return (
    <div className="App">
        <Navbar/>
        <Introduction/>
        <Detector/>
    </div>
  );
}

export default App;
