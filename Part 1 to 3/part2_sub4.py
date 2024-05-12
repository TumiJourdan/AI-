import chess
import reconchess.utilities as rutils

def is_consistent_with_window(state_fen, window):
    board = chess.Board(state_fen)

    observations = window.split(";")
    for observation in observations:
        square, piece = observation.split(":")
        square_index = chess.parse_square(square)
        observed_piece = piece.lower() if piece.islower() else piece.upper()

        if board.piece_at(square_index):
            current_piece = str(board.piece_at(square_index)).lower() if str(board.piece_at(square_index)).islower() else str(board.piece_at(square_index)).upper()
            if current_piece != observed_piece:
                return False
        else:
            if observed_piece != '?':
                return False

    return True

def filter_states(states, window):
    consistent_states = []
    for state in states:
        if is_consistent_with_window(state, window):
            consistent_states.append(state)
    return sorted(consistent_states)

def main():

    num_states = int(input())

    potential_states = [input() for _ in range(num_states)]
    
    window = input()
    
    consistent_states = filter_states(potential_states, window)
    
    for state in consistent_states:
        print(state)

if __name__ == "__main__":
    main()
