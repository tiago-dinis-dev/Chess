import React from 'react';
import Chessboard from 'chessboardjsx';

function ChessGame() {
  return (
    <div>
      <Chessboard
        position="start"
        width={320}
      />
    </div>
  );
}

export default ChessGame;