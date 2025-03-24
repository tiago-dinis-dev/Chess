import React, { useCallback, useState, useMemo } from 'react';
import { Chessboard } from 'react-chessboard';
import { Chess } from 'chess.js';

function ChessGame() {
  const chess = useMemo(() => new Chess(), []);
  const [fen, setFen] = useState(chess.fen());
  const [over, setOver] = useState("");

  function onDrop(sourceSquare, targetSquare) {
    const moveData = {
      from: sourceSquare,
      to: targetSquare,
      color: chess.turn(),
      promotion: 'q',
    };

    const move = makeAMove(moveData);

    return move !== null;
  }

  const makeAMove = useCallback(
    (move) => {
      try {
        const result = chess.move(move);
        setFen(chess.fen());

        console.log("over, checkmate", chess.isGameOver(), chess.isCheckmate());

        if (chess.isGameOver){
          if(chess.isCheckmate()){
            setOver(`Checkmate! ${chess.turn() === "w" ? "black" : "white"} wins!`);
          }
          else if (chess.isDraw()){
            setOver("Draw!");
          }
          else {
            setOver("Stalemate!");
          }
        }

        return result;
      } catch(e) {
        return null;
      }
    },
    [chess]
  );

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%' }}>
      <Chessboard
        position={fen}
        boardWidth={520}
        onPieceDrop={onDrop}
        draggable={true}
        showBoardNotation={true}
      />
    </div>
  );
}

export default ChessGame;