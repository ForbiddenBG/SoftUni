def is_inside(n_row, n_col, mat):
    return 0 <= n_row < len(mat) and 0 <= n_col < len(mat)


def calc_next_move(row_idx, col_idx, matrx):
    initial_row, initial_col = row_idx, col_idx
    while is_inside(row_idx-1, col_idx, matrx) and matrx[row_idx-1][col_idx] != "Q":
        row_idx, col_idx = row_idx-1, col_idx
        if matrx[row_idx][col_idx] == "K":
            return True
    row_idx, col_idx = initial_row, initial_col
    while is_inside(row_idx-1, col_idx+1, matrx) and matrx[row_idx-1][col_idx+1] != "Q":
        row_idx, col_idx = row_idx-1, col_idx+1
        if matrx[row_idx][col_idx] == "K":
            return True
    row_idx, col_idx = initial_row, initial_col
    while is_inside(row_idx, col_idx+1, matrx) and matrx[row_idx][col_idx+1] != "Q":
        row_idx, col_idx = row_idx, col_idx+1
        if matrx[row_idx][col_idx] == "K":
            return True
    row_idx, col_idx = initial_row, initial_col
    while is_inside(row_idx+1, col_idx+1, matrx) and matrx[row_idx+1][col_idx+1] != "Q":
        row_idx, col_idx = row_idx+1, col_idx+1
        if matrx[row_idx][col_idx] == "K":
            return True
    row_idx, col_idx = initial_row, initial_col
    while is_inside(row_idx+1, col_idx, matrx) and matrx[row_idx+1][col_idx] != "Q":
        row_idx, col_idx = row_idx+1, col_idx
        if matrx[row_idx][col_idx] == "K":
            return True
    row_idx, col_idx = initial_row, initial_col
    while is_inside(row_idx+1, col_idx-1, matrx) and matrx[row_idx+1][col_idx-1] != "Q":
        row_idx, col_idx = row_idx+1, col_idx-1
        if matrx[row_idx][col_idx] == "K":
            return True
    row_idx, col_idx = initial_row, initial_col
    while is_inside(row_idx, col_idx-1, matrx) and matrx[row_idx][col_idx-1] != "Q":
        row_idx, col_idx = row_idx, col_idx-1
        if matrx[row_idx][col_idx] == "K":
            return True
    row_idx, col_idx = initial_row, initial_col
    while is_inside(row_idx-1, col_idx-1, matrx) and matrx[row_idx-1][col_idx-1] != "Q":
        row_idx, col_idx = row_idx-1, col_idx-1
        if matrx[row_idx][col_idx] == "K":
            return True
    return False


size = 8

matrix = []

for row in range(size):
    matrix.append(input().split())

queens = []

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == "Q":
            if calc_next_move(row_index, col_index, matrix):
                queens.append([row_index, col_index])

if not queens:
    print("The king is safe!")
else:
    for row in queens:
        print(row)
