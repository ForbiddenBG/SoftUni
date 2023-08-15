def is_inside(n_row, n_col, ma):
    return 0 <= n_row < len(ma) and 0 <= n_col < len(ma)


def calc_next_pos(p_row, p_col, comm):
    if comm == "up":
        return p_row-1, p_col
    if comm == "right":
        return p_row, p_col+1
    if comm == "down":
        return p_row+1, p_col
    if comm == "left":
        return p_row, p_col-1


string = input()

size = int(input())

matrix = []

player_row, player_col = 0, 0

for row in range(size):
    matrix.append([x for x in input()])
    for col in range(size):
        if matrix[row][col] == "P":
            player_row, player_col = row, col

turns = int(input())

for _ in range(turns):
    command = input()
    matrix[player_row][player_col] = "-"
    next_row, next_col = calc_next_pos(player_row, player_col, command)
    if is_inside(next_row, next_col, matrix):
        if matrix[next_row][next_col].isalpha():
            string += matrix[next_row][next_col]
        if matrix[next_row][next_col] == "-":
            pass
        matrix[next_row][next_col] = "P"
        player_row, player_col = next_row, next_col
    else:
        if string:
            string = string[:-1]
        matrix[player_row][player_col] = "P"

print(string)
for row in matrix:
    print(*row, sep="")
