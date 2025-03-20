import axios from 'axios';

async function sendMove(move) {
  await axios.post('/api/move/', {
    move: move.san // send the move in Standard Algebraic Notation (SAN)
  });
}
