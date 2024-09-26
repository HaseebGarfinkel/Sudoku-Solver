# function to ensure that a placed value is not repeated in the row, column, and sub grid

def validate_placement(row, col, value):
    if value not in row:
        if value not in col:
            return True


