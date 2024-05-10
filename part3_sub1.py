import chess.engine
# engine = chess.engine.SimpleEngine.popen_uci('./stockfish', setpgrp=True)
engine = chess.engine.SimpleEngine.popen_uci('/opt/stockfish/stockfish', setpgrp=True)

def capture_opponent_king(board):
    for move in board.legal_moves:
        if board.is_capture(move) and board.piece_at(move.to_square) == chess.KING:
            return move.uci()
    return None

def select_move_with_stockfish(board):
    result = engine.play(board, chess.engine.Limit(time=0.5))
    engine.quit()
    return result.move.uci()

def select_move(board):
    capture_move = capture_opponent_king(board)
    if capture_move:
        return capture_move

    return select_move_with_stockfish(board)

def main():
    fen_input = input() 
    board = chess.Board(fen_input)  
    move = select_move(board)  
    print(move)
    

if __name__ == "__main__":
    main()








