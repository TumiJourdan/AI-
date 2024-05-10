import chess
import reconchess.utilities as rutils

# def generate_next_moves(board):
#     next_moves = set() 

#     pseudolegal_moves = board.pseudo_legal_moves
#     for move in pseudolegal_moves:
#         next_moves.add(move.uci())

#     next_moves.add(str(chess.Move.null()))
    
#     for move in rutils.without_opponent_pieces(board).generate_castling_moves():
#         if not rutils.is_illegal_castle(board, move):
#             next_moves.add(move.uci())

#     return sorted(next_moves)

def StatePredSense(states, window):
    boards = []
    
    possible_states = []
    
    for i in states:
        boards.append(chess.Board(i))

    windowSquares = window.split(';')
    
    
    for curr_board in boards:
        for i, squares in enumerate(windowSquares):
            square_piece = squares.split(':')
            
            square = chess.square(square_piece[0])
            
            if square_piece[1] == '?':
                square_piece[1] = 'None'
            
            
            if curr_board.piece_at(square) != square_piece[1]:
                break
            else:
                possible_states.append(states[i])
                
    return possible_states
            
        
            
        


def main():
    states = []
    
    n = int(input())
    
    for i in range(n):
        states.append(input())
        
    window = input()
    
    pos_states = StatePredSense(states, window)
    sorted_states = sorted(pos_states)
    for state in sorted_states:
        print(state)
    
    
    
    # next_moves = generate_next_moves(board)
    
    
    
    # capture_moves = []
    
    # for move in next_moves:
    #     if (move[2:4] == capture_move):
    #         capture_moves.append(move)
    
    
    # for move in capture_moves:
    #     move = chess.Move.from_uci(move)
    #     board_ins = chess.Board(fen_input)
    #     board_ins.push(move)
    #     next_states.add(board_ins.fen())

    # sorted_states = sorted(next_states)
    # for state in sorted_states:
    #     print(state)
        

if __name__ == "__main__":
    main()
