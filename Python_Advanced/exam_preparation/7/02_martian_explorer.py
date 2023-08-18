def is_inside(r, c, ma):
    return 0 <= r < ma and 0 <= c < ma


def calc_next_pos(ro, co, siz, comm):
    if comm == "up":
        if is_inside(ro-1, co, siz):
            return ro-1, co
        else:
            return siz-1, co
    if comm == "right":
        if is_inside(ro, co+1, siz):
            return ro, co+1
        else:
            return ro, 0
    if comm == "down":
        if is_inside(ro+1, co, siz):
            return ro+1, co
        else:
            return 0, co
    if comm == "left":
        if is_inside(ro, co-1, siz):
            return ro, co-1
        else:
            return ro, siz-1


size = 6

matrix = []

row_index, col_index = 0, 0

for row in range(size):
    matrix.append([x for x in input().split()])
    for col in range(size):
        if matrix[row][col] == "E":
            row_index, col_index = row, col

commands = input().split(", ")
deposits = {"Water": 0, "Metal": 0, "Concrete": 0}

for command in commands:
    matrix[row_index][col_index] = "-"
    next_row, next_col = calc_next_pos(row_index, col_index, size, command)
    if matrix[next_row][next_col] == "W":
        print(f"Water deposit found at ({next_row}, {next_col})")
        deposits["Water"] += 1
    elif matrix[next_row][next_col] == "M":
        print(f"Metal deposit found at ({next_row}, {next_col})")
        deposits["Metal"] += 1
    elif matrix[next_row][next_col] == "C":
        print(f"Concrete deposit found at ({next_row}, {next_col})")
        deposits["Concrete"] += 1
    elif matrix[next_row][next_col] == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break
    row_index, col_index = next_row, next_col


if deposits["Water"] >= 1 and deposits["Metal"] >= 1 and deposits["Concrete"] >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
