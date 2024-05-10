import chess
import reconchess.utilities as rutils

def generate_next_moves( board):
    next_moves = set() 

    pseudolegal_moves = board.pseudo_legal_moves
    for move in pseudolegal_moves:
        next_moves.add(move.uci())

    next_moves.add(str(chess.Move.null()))
    
    for move in rutils.without_opponent_pieces(board).generate_castling_moves():
        if not rutils.is_illegal_castle(board, move):
            next_moves.add(move.uci())

    return sorted(next_moves)

def main():
    next_states = set() 
    fen_input = input()
    capture_move = input()
    board = chess.Board(fen_input)
    next_moves = generate_next_moves(board)
    
    capture_moves = []
    
    for move in next_moves:
        if (move[2:4] == capture_move):
            capture_moves.append(move)
    
    
    for move in capture_moves:
        move = chess.Move.from_uci(move)
        board_ins = chess.Board(fen_input)
        board_ins.push(move)
        next_states.add(board_ins.fen())

    sorted_states = sorted(next_states)
    for state in sorted_states:
        print(state)
        

if __name__ == "__main__":
    main()
