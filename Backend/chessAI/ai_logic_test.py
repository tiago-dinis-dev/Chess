import unittest
import chess
from .ai_logic import evaluate_board, minimax, select_best_move

class TestAILogic(unittest.TestCase):
    def test_evaluate_board_starting_position(self):
        """Test evaluate_board with the starting position."""
        board = chess.Board()
        score = evaluate_board(board)
        self.assertEqual(score, 0, "Starting position should have a score of 0")

    def test_evaluate_board_material_advantage(self):
        """Test evaluate_board with a material advantage for white."""
        board = chess.Board("8/8/8/8/8/8/8/4Q3 w - - 0 1")  # White has a queen
        score = evaluate_board(board)
        self.assertEqual(score, 9, "White should have a score of 9 for the queen")

        board = chess.Board("8/8/8/8/8/8/8/4q3 b - - 0 1")  # Black has a queen
        score = evaluate_board(board)
        self.assertEqual(score, -9, "Black should have a score of -9 for the queen")

    def test_minimax_depth_0(self):
        """Test minimax with depth 0."""
        board = chess.Board()
        score = minimax(board, depth=0, is_maximizing=True)
        self.assertEqual(score, 0, "Minimax at depth 0 should return the evaluation score")

    def test_minimax_game_over(self):
        """Test minimax when the game is over."""
        board = chess.Board("8/8/8/8/8/8/8/K7 w - - 0 1")  # White king only
        board.push(chess.Move.from_uci("a1a2"))  # Stalemate
        score = minimax(board, depth=2, is_maximizing=True)
        self.assertEqual(score, 0, "Minimax should return 0 for a stalemate")

    def test_select_best_move_starting_position(self):
        """Test select_best_move with the starting position."""
        board = chess.Board()
        move = select_best_move(board, depth=1)
        self.assertIsNotNone(move, "select_best_move should return a valid move")
        self.assertIn(move, board.legal_moves, "The selected move should be legal")

    def test_select_best_move_checkmate(self):
        """Test select_best_move when a checkmate is possible."""
        board = chess.Board("rnb1kbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")  # Simplified position
        move = select_best_move(board, depth=1)
        self.assertIsNotNone(move, "select_best_move should return a valid move")
        board.push(move)
        self.assertFalse(board.is_checkmate(), "The move should not result in an immediate checkmate")

if __name__ == "__main__":
    unittest.main()