#!/usr/bin/python3
'''N Queens problem.'''


def is_safe(board, row, col):
    '''Checks if position is safe from attack.

    Args:
        board: board state.
        row: row to check.
        col: colum to check.
    '''
    for i in range(col):
        if board[i] is row or abs(board[i] - row) is abs(i - col):
            return False
        return True


def nchecker(board, col):
    '''
    Args:
        board: The board state.
        col: The current colum to check.
    '''
    j = len(board)
    if col is j:
        print(str([[i, board[i]] for i in range(j)]))
        return

    for row in range(j):
        if is_safe(board, row, col):
            board[col] = row
            nchecker(board, col + 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    j = 0
    try:
        j = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if j < 4:
        print("N must be at least 4")
        sys.exit(1)
        board = [0 for col in range(j)]
        nchecker(board, 0)
