import React, { Component } from 'react'
import ChessBoard from './ChessBoard'
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Welcome to Chess</h2>
        </div>
        <div className="App-intro">
          <ChessBoard />
        </div>
      </div>
    );
  }
}

export default App;
