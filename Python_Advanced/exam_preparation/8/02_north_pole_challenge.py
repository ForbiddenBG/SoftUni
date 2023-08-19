def is_inside(r, c, mat_row, mat_col):
    return 0 <= r < mat_row and 0 <= c < mat_col


def calc_new_pos(row, col, dir, ma_r, ma_c):
    if dir == "up":
        if is_inside(row-1, col, ma_r, ma_c):
            return row-1, col
        else:
            return ma_r-1, col
    if dir == "right":
        if is_inside(row, col+1, ma_r, ma_c):
            return row, col+1
        else:
            return row, 0
    if dir == "down":
        if is_inside(row+1, col, ma_r, ma_c):
            return row+1, col
        else:
            return 0, col
    if dir == "left":
        if is_inside(row, col-1, ma_r, ma_c):
            return row, col-1
        else:
            return row, ma_c-1


x, y = input().split(", ")
rows, cols = int(x), int(y)

matrix = []

position_row, position_col = 0, 0
total_count = {"Christmas decorations": 0, "Gifts": 0, "Cookies": 0}

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == "Y":
            position_row, position_col = row, col
        if matrix[row][col] == "D":
            total_count["Christmas decorations"] += 1
        elif matrix[row][col] == "G":
            total_count["Gifts"] += 1
        elif matrix[row][col] == "C":
            total_count["Cookies"] += 1

collectables = {"Christmas decorations": 0, "Gifts": 0, "Cookies": 0}
is_Christmas = False

command = input()
while command != "End":
    direction, step = command.split("-")
    step = int(step)
    for move in range(step):
        matrix[position_row][position_col] = "x"
        new_row, new_col = calc_new_pos(position_row, position_col, direction, rows, cols)
        if matrix[new_row][new_col] == "D":
            collectables["Christmas decorations"] += 1
            total_count["Christmas decorations"] -= 1
        if matrix[new_row][new_col] == "G":
            collectables["Gifts"] += 1
            total_count["Gifts"] -= 1
        if matrix[new_row][new_col] == "C":
            collectables["Cookies"] += 1
            total_count["Cookies"] -= 1
        position_row, position_col = new_row, new_col
        matrix[position_row][position_col] = "Y"
        if sum(total_count.values()) == 0:
            print("Merry Christmas!")
            matrix[position_row][position_col] = "Y"
            is_Christmas = True
            break
    if is_Christmas:
        break

    command = input()

print("You've collected:")
for k, v in collectables.items():
    print(f"- {v} {k}")

for row in matrix:
    print(*row)
