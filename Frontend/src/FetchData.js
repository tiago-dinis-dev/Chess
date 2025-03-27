import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000';

export const startGame = async (playerWhite, playerBlack) => {
  const response = await axios.post(`${BASE_URL}/games/start_game/`, {
    player_white: playerWhite,
    player_black: playerBlack
  });
  return response.data;
};

export const postMove = async (gameId, moveNumber, moveNotation) => {
  await axios.post(`${BASE_URL}/moves/`, {
    game: gameId,
    move_number: moveNumber,
    move_notation: moveNotation
  });
};

export const updateStatus = async (gameId, status) => {
  await axios.patch(`${BASE_URL}/games/${gameId}/update_status/`, {
    status: status
  });
};

export const getAIMove = async (fen) => {
  const response = await axios.post(`${BASE_URL}/ai/move/`, {
    board: fen
  });
  return response.data;
};