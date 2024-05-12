import chess.engine
import random
from reconchess import *

class MyAgent(Player):
    def __init__(self):
        self.board = None
        self.color = None
        self.my_piece_captured_square = None
        self.possible_states = set()
        self.engine = chess.engine.SimpleEngine.popen_uci('./stockfish', setpgrp=True)

    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        self.board = board
        self.color = color
        self.possible_states = {board.fen()}

    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        self.my_piece_captured_square = capture_square
        if captured_my_piece:
            self.possible_states = {state for state in self.possible_states if self.board.set_fen(state) and self.board.remove_piece_at(capture_square)}
        else:
            self.possible_states = {state for state in self.possible_states if self.board.set_fen(state) and not any(self.board.is_capture(move) for move in self.board.pseudo_legal_moves)}

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> Optional[Square]:
    # Exclude squares on the perimeter of the board
        valid_sense_actions = [square for square in sense_actions if square not in [
            chess.A1, chess.A2, chess.A3, chess.A4, chess.A5, chess.A6, chess.A7, chess.A8,
            chess.B1, chess.B8,
            chess.C1, chess.C8,
            chess.D1, chess.D8,
            chess.E1, chess.E8,
            chess.F1, chess.F8,
            chess.G1, chess.G8,
            chess.H1, chess.H2, chess.H3, chess.H4, chess.H5, chess.H6, chess.H7, chess.H8
        ]]
        return random.choice(valid_sense_actions) if valid_sense_actions else None

    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        self.possible_states = {state for state in self.possible_states if all(self.board.piece_at(square) == piece for square, piece in sense_result)}

    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        if len(self.possible_states) > 10000:
            self.possible_states = set(random.sample(self.possible_states, 10000))

        n = len(self.possible_states)
        time_limit = 10 / n if n > 0 else 0.1

        move_counts = {}
        for state in self.possible_states:
            self.board.set_fen(state)
            result = self.engine.play(self.board, chess.engine.Limit(time=time_limit))
            move = result.move
            move_counts[move] = move_counts.get(move, 0) + 1

        if move_counts:
            return max(move_counts, key=move_counts.get)
        else:
            return random.choice(move_actions)

    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move], captured_opponent_piece: bool, capture_square: Optional[Square]):
        if taken_move is not None:
            self.possible_states = {state for state in self.possible_states if self.board.push(taken_move)}

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason], game_history: GameHistory):
        self.engine.quit()