import os
import sys
import numpy as np
import chess

# Define functions
def main():
    inString = []
    while True:
        line = input()
        if line == '':  # Check if the line is empty
            break
        inString.append(line)
    board = chess.Board(inString[0])
    move = chess.Move.from_uci(inString[1])
    board.push(move)
    print(board.fen())

# Entry point of the script
if __name__ == "__main__":
    main()