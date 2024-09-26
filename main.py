sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def print_board(board):
    for row in board:
        print(row)


print_board(sudoku_board)


def validate_placement(y, x, value):  # constraint: make sure value is not already in row, col, sub grid

    if value in sudoku_board[y]:  # return false if the number is already in the row
        return False
    for rows in sudoku_board:
        if rows[x] == value:  # return false if the number is already in the column
            return False
    sub_row = (y // 3) * 3  # return false if the number is already in the sub grid
    sub_col = (x // 3) * 3
    for i in range(sub_row, sub_row + 3):
        for j in range(sub_col, sub_col + 3):
            if sudoku_board[i][j] == value:
                return False
    return True


def empty_space():  # find empty space in board and return the row and column of that space
    for row in sudoku_board:
        for num in row:
            if num == 0:
                val_row = sudoku_board.index(row)
                val_col = row.index(num)
                return val_row, val_col
    return False


def cell_solve():
    if not empty_space():
        return True
    row, col = empty_space()
    for value in range(10):
        if validate_placement(row, col, value):
            sudoku_board[row][col] = value
            if cell_solve():
                return True
        print(row, col)
        sudoku_board[row][col] = 0


cell_solve()
print("""


""")

print_board(sudoku_board)
