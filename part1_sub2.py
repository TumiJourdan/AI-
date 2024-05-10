import os
import sys
import numpy as np
import chess

# Define functions
def main():
    inString = [0,0]
    inString[0] = input()
    inString[1] = input()
    board = chess.Board(inString[0])
    move = chess.Move.from_uci(inString[1])
    board.push(move)
    print(board.fen())

# Entry point of the script
if __name__ == "__main__":
    main()