#!/usr/bin/python3
"""

N-Queens Puzzle

"""


import sys


def is_safe(board, row, col, N):
    """
       >> Check for queens in the same column.
    """
    for i in range(row):
        if board[i] == col or \
              board[i] - i == col - row or \
              board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []

    def backtrack(row, board):
        if row == N:
            solutions.append(board[:])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1, board)

    backtrack(0, [-1] * N)

    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == "__main__":
    main()
