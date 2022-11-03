#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard
"""
from sys import argv, exit


def queens(N, row, col, solutions):
    """
    Set queens on N-board recursevily to find the solutions
    """
    while col < N:
        if solve(row, col, solutions):
            solutions.append([row, col])
            if row == (N - 1):
                print(solutions)
                solutions.pop()
            else:
                queens(N, row + 1, 0, solutions)
        col += 1
    if len(solutions) > 0:
        solutions.pop()


def solve(row, col, solutions):
    """
    Get valid queens positions
    """
    valid = True
    rows = [s[0] for s in solutions]
    cols = [s[1] for s in solutions]
    dgn1 = [s[0] + s[1] for s in solutions]
    dgn2 = [s[1] - s[0] for s in solutions]
    if row in rows or col in cols or \
            (row + col) in dgn1 or (col - row) in dgn2:
        valid = False
    return valid


if __name__ == "__main__":
    length = len(argv)
    if length != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)
    queens(N, 0, 0, [])