import { Chess } from 'chess.js';

const chess = new Chess();

function makeMove(sourceSquare, targetSquare) {
  // Check if the move is valid
  const move = chess.move({
    from: sourceSquare,
    to: targetSquare,
    promotion: 'q' // Default to queen promotion
  });

  if (move === null) return false; // Invalid move
  return move;
}
