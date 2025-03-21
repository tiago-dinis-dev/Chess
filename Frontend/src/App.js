import './App.css';
import React from 'react';
import ChessGame from './components/Chessboard';

function App() {
  return (
      <div className="App">
        <header className="App-header">
          <ChessGame />
        </header>
      </div>
  );
}

export default App;
