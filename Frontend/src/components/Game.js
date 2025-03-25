import React, { useCallback, useState, useMemo, useEffect } from 'react';
import { Chessboard } from 'react-chessboard';
import { Chess } from 'chess.js';
import { startGame, postMove, updateStatus } from '../FetchData';

function ChessGame() {
  const chess = useMemo(() => new Chess(), []);
  const [fen, setFen] = useState(chess.fen());
  const [over, setOver] = useState("");
  const [gameId, setGameId] = useState(null);

  useEffect(() => {
    async function initializeGame() {
      const data = await startGame('Player 1', 'Player 2');
      setGameId(data.game_id);
    }
    initializeGame();
  }, []);

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
    async (move) => {
      try {
        const result = chess.move(move);
        setFen(chess.fen());

        if (result) {
          await postMove(gameId, chess.history().length, result.san);
        }

        if (chess.isGameOver()) {
          let status = '';
          if (chess.isCheckmate()) {
            status = 'checkmate';
            setOver(`Checkmate! ${chess.turn() === "w" ? "black" : "white"} wins!`);
          } else if (chess.isDraw()) {
            status = 'draw';
            setOver("Draw!");
          } else {
            status = 'stalemate';
            setOver("Stalemate!");
          }
          await updateStatus(gameId, status);
        }

        return result;
      } catch (e) {
        return null;
      }
    },
    [chess, gameId]
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