# function solves one cell of the sudoku board
from validate_placement import validate_placement


def cell_solve(board, row, col):
    # choice: testing all possible numbers 1 through 9 for value
    for value in range(1, 10):
        board[row][col] = value
        # constraint: make sure value is not already in row, column, sub grid
        if validate_placement(row, col, value):
            break
    board[row][col] = 0

