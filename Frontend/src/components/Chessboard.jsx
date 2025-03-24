import React from 'react';
import { Chessboard } from 'react-chessboard';

function ChessGame() {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%' }}>
      <Chessboard
        position="start"
        boardWidth={520}
      />
    </div>
  );
}

export default ChessGame;