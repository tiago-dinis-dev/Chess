import chess  
import random

# Enhanced evaluation function for a position
def evaluate_board(board):
    """Evaluates the current board position and returns a score."""
    material_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3.5,
        chess.ROOK: 5,
        chess.QUEEN: 9,
    }
    
    # Positional values for pawns (example, can be expanded for other pieces)
    pawn_position_values = [
        0, 0, 0, 0, 0, 0, 0, 0,
        0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1,
        0.05, 0.05, 0.1, 0.25, 0.25, 0.1, 0.05, 0.05,
        0, 0, 0, 0.2, 0.2, 0, 0, 0,
        0.05, -0.05, -0.1, 0, 0, -0.1, -0.05, 0.05,
        0.05, 0.1, 0.1, -0.2, -0.2, 0.1, 0.1, 0.05,
        0, 0, 0, 0, 0, 0, 0, 0
    ]

    score = 0
    for square, piece in board.piece_map().items():
        piece_value = material_values.get(piece.piece_type, 0)
        if piece.color == chess.WHITE:
            score += piece_value
            if piece.piece_type == chess.PAWN:
                score += pawn_position_values[square]
        else:
            score -= piece_value
            if piece.piece_type == chess.PAWN:
                score -= pawn_position_values[chess.square_mirror(square)]
    
    # Penalize repetitive moves
    if board.is_repetition(2):
        score -= 0.5 if board.turn == chess.WHITE else -0.5

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
