import React, { useCallback, useState, useMemo, useEffect } from 'react';
import { Chessboard } from 'react-chessboard';
import { Chess } from 'chess.js';
import { startGame, postMove, updateStatus, getAIMove } from '../FetchData';

function ChessGame() {
  const chess = useMemo(() => new Chess(), []);
  const [fen, setFen] = useState(chess.fen());
  const [over, setOver] = useState("");
  const [gameId, setGameId] = useState(null);
  const [playerColor, setPlayerColor] = useState(null);
  const [gameStarted, setGameStarted] = useState(false);

  const handleMove = useCallback(
    async (move, isAI = false) => {
      try {
        let result;

        if (isAI) {
          const data = await getAIMove(chess.fen());
          result = chess.move(data.best_move);
        } else {
          result = chess.move(move);
        }

        if (result) {
          setFen(chess.fen());
          await postMove(gameId, chess.history().length, result.san);

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
        }

        return result;
      } catch (error) {
        console.error("Error handling move:", error);
        return null;
      }
    },
    [chess, fen, gameId]
  );

  useEffect(() => {
    async function initializeGame() {
      const data = await startGame('Player 1', 'Player 2');
      setGameId(data.game_id);

      if (playerColor === 'b') {
        setTimeout(async () => {
          const data = await getAIMove(chess.fen());
          const aiMove = chess.move(data.best_move);
          if (aiMove) {
            setFen(chess.fen());
            await postMove(data.game_id, chess.history().length, aiMove.san);
          }
        }, 200); 
      }
    }

    if (gameStarted) {
      initializeGame();
    }
  }, [gameStarted, playerColor]);

  function onDrop(sourceSquare, targetSquare) {
    if (!gameStarted) return false;

    const moveData = {
      from: sourceSquare,
      to: targetSquare,
      color: playerColor,
      promotion: 'q',
    };

    const move = handleMove(moveData);

    if (move !== null && chess.turn() !== playerColor) {
      setTimeout(() => {
        handleMove(null, true); 
      }, 200); 
    }
    
    return move !== null;
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%' }}>
      {!gameStarted ? (
        <div>
          <h2>Choose Your Color</h2>
          <button onClick={() => { setPlayerColor('w'); setGameStarted(true); }}>Play as White</button>
          <button onClick={() => { setPlayerColor('b'); setGameStarted(true); }}>Play as Black</button>
        </div>
      ) : (
        <>
          <Chessboard
            position={fen}
            boardWidth={520}
            onPieceDrop={onDrop}
            draggable={true}
            showBoardNotation={true}
            boardOrientation={playerColor === 'w' ? 'white' : 'black'}
          />
          {over && <div style={{ marginTop: '20px', color: 'red' }}>{over}</div>}
        </>
      )}
    </div>
  );
}

export default ChessGame;