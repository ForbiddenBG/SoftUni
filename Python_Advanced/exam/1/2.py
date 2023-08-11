def is_inside(r, c, m):
    return 0 <= r < len(m) and 0 <= c < len(m)


def calc_next_move(row, col, ma, massive):
    if "White" in massive:
        if is_inside(row - 1, col + 1, ma) and ma[row - 1][col + 1] == "b":
            return row - 1, col + 1
        if is_inside(row - 1, col - 1, ma) and ma[row - 1][col - 1] == "b":
            return row - 1, col - 1
        else:
            return row - 1, col
    if "Black" in massive:
        if is_inside(row + 1, col + 1, ma) and ma[row + 1][col + 1] == "w":
            return row + 1, col + 1
        if is_inside(row + 1, col - 1, ma) and ma[row + 1][col - 1] == "w":
            return row + 1, col - 1
        else:
            return row + 1, col


def calc_square(letters_massive, columns_massive, row, col):
    result = ""
    for k, v in letters_massive.items():
        if col == v:
            result += f"{k}"
            for k, v in columns_massive.items():
                if row == k:
                    result += f"{v}"
    return result


size = 8

matrix = []

white_row, white_col = 0, 0
black_row, black_col = 0, 0

for row in range(size):
    matrix.append([x for x in input().split()])
    for col in range(size):
        if matrix[row][col] == "w":
            white_row, white_col = row, col
        elif matrix[row][col] == "b":
            black_row, black_col = row, col

letters = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

columns = {
    7: 1,
    6: 2,
    5: 3,
    4: 4,
    3: 5,
    2: 6,
    1: 7,
    0: 8
}

peons = []

for move in range(16):
    if move % 2 == 0:
        peons.append("White")
        next_row, next_col = calc_next_move(white_row, white_col, matrix, peons)
        matrix[white_row][white_col] = "-"
        if matrix[next_row][next_col] == "b":
            matrix[next_row][next_col] = "w"
            result = calc_square(letters, columns, next_row, next_col)
            print(f"Game over! White win, capture on {result}.")
            break
        if next_row == 0:
            matrix[next_row][next_col] = "w"
            result = calc_square(letters, columns, next_row, next_col)
            print(f"Game over! White pawn is promoted to a queen at {result}.")
            break
        else:
            matrix[next_row][next_col] = "w"
        white_row, white_col = next_row, next_col
    elif move % 2 == 1:
        peons.append("Black")
        next_row, next_col = calc_next_move(black_row, black_col, matrix, peons)
        matrix[black_row][black_col] = "-"
        if matrix[next_row][next_col] == "w":
            matrix[next_row][next_col] = "b"
            result = calc_square(letters, columns, next_row, next_col)
            print(f"Game over! Black win, capture on {result}.")
            break
        if next_row == 7:
            matrix[next_row][next_col] = "b"
            result = calc_square(letters, columns, next_row, next_col)
            print(f"Game over! Black pawn is promoted to a queen at {result}.")
            break
        else:
            matrix[next_row][next_col] = "b"
        black_row, black_col = next_row, next_col
    peons.pop()
