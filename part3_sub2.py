import chess.engine
from collections import Counter

# engine = chess.engine.SimpleEngine.popen_uci('./stockfish', setpgrp=True)
# # engine = chess.engine.SimpleEngine.popen_uci('/opt/stockfish/stockfish', setpgrp=True)

def capture_opponent_king(board):
    for move in board.legal_moves:
        if board.is_capture(move) and board.piece_at(move.to_square) == chess.KING:
            return move.uci()
    return None

def select_move_with_stockfish(board):
    engine = chess.engine.SimpleEngine.popen_uci('./stockfish', setpgrp=True)
    # engine = chess.engine.SimpleEngine.popen_uci('/opt/stockfish/stockfish', setpgrp=True)
    result = engine.play(board, chess.engine.Limit(time=0.5))
    engine.quit()
    return result.move.uci()

def select_move(board):
    capture_move = capture_opponent_king(board)
    if capture_move:
        return capture_move

    return select_move_with_stockfish(board)

def main():
    num_boards = int(input())
    boards = [input() for _ in range(num_boards)]
    
    moves = []
    for fen in boards:
        board = chess.Board(fen)
        move = select_move(board)
        moves.append(move)
    
    move_counts = Counter(moves)
    
 
    max_count = max(move_counts.values())
    most_common_moves = [move for move, count in move_counts.items() if count == max_count]
  
    selected_move = sorted(most_common_moves)[0]
    
    print(selected_move)

if __name__ == "__main__":
    main()








