import './App.css';
import React from 'react';
import ChessGame from './components/Game.js';

export default function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Chess Game</h1>  
      </header>
      <div className="App-body">
        <ChessGame />
      </div>
    </div>
  );
}
