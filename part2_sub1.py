import chess
import reconchess.utilities as rutils

def generate_next_moves(fen):
    board = chess.Board(fen)
    next_moves = set() 

    pseudolegal_moves = board.pseudo_legal_moves
    for move in pseudolegal_moves:
        next_moves.add(move.uci())

    next_moves.add("0000")

    for move in rutils.without_opponent_pieces(board).generate_castling_moves():
        if not rutils.is_illegal_castle(board, move):
            next_moves.add(move.uci())

    return sorted(next_moves)

def main():
    fen_input = input()
    next_moves = generate_next_moves(fen_input)
    for move in next_moves:
        print(move)

if __name__ == "__main__":
    main()
