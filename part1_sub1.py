import os
import sys
import numpy as np
import chess

# Define functions
def main():
    inString = [0]
    inString[0] = input()
    board = chess.Board(inString[0])
    print(board)

# Entry point of the script
if __name__ == "__main__":
    main()