from math import floor


def is_inside(p_r, p_c, ma):
    return 0 <= p_r < len(ma) and 0 <= p_c < len(ma)


def calc_new_pos(p_row, p_col, comm, matrx, siz):
    if comm == "up":
        if is_inside(p_row-1, p_col, matrx):
            return p_row-1, p_col
        else:
            return siz-1, p_col
    if comm == "right":
        if is_inside(p_row, p_col+1, matrx):
            return p_row, p_col+1
        else:
            return p_row, 0
    if comm == "down":
        if is_inside(p_row+1, p_col, matrx):
            return p_row+1, p_col
        else:
            return 0, p_col
    if comm == "left":
        if is_inside(p_row, p_col-1, matrx):
            return p_row, p_col-1
        else:
            return p_row, siz-1


size = int(input())

matrix = []

player_row, player_col = 0, 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "P":
            player_row, player_col = row, col

moves = []
coins = 0
is_won = False
moves.append([player_row, player_col])

command = input()
while True:
    matrix[player_row][player_col] = "0"
    next_row, next_col = calc_new_pos(player_row, player_col, command, matrix, size)
    if matrix[next_row][next_col].isdigit():
        coins += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = "P"
    player_row, player_col = next_row, next_col
    moves.append([player_row, player_col])
    if matrix[next_row][next_col] == "X":
        coins *= 0.5
        break
    if coins >= 100:
        is_won = True
        print(f"You won! You've collected {floor(coins)} coins.")
        break
    command = input()

if not is_won:
    print(f"Game over! You've collected {floor(coins)} coins.")

print("Your path:")
for row in moves:
    print(row)
