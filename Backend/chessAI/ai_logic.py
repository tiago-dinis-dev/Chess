import chess  
import random

# Simple evaluation function for a position (this will get more complex)
def evaluate_board(board):
    """Evaluates the current board position and returns a score."""
    # Here we could use material count as a basic evaluation
    material_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
    }
    
    score = 0
    for piece in board.piece_map().values():
        if piece.color == chess.WHITE:
            score += material_values.get(piece.piece_type, 0)
        else:
            score -= material_values.get(piece.piece_type, 0)
    
    return score

# Minimax algorithm (basic version)
def minimax(board, depth, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if is_maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval

# AI move selection
def select_best_move(board, depth=2):
    """Selects the best move for the AI using Minimax."""
    best_move = None
    best_value = float('-inf')
    
    for move in board.legal_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, False)
        board.pop()
        
        if board_value > best_value:
            best_value = board_value
            best_move = move
    
    return best_move or random.choice(list(board.legal_moves))  # Fallback if no move is found
