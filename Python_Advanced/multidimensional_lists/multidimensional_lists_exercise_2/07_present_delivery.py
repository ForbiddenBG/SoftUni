def get_new_pos(r, c, comm):
    if comm == "up":
        return r-1, c
    if comm == "right":
        return r, c+1
    if comm == "down":
        return r+1, c
    if comm == "left":
        return r, c-1


num_presents = int(input())
size = int(input())

matrix = []

santa_row, santa_col = 0, 0
total_nice = 0

for row in range(size):
    matrix.append([x for x in input().split()])
    for col in range(size):
        if matrix[row][col] == "S":
            santa_row, santa_col = row, col
        if matrix[row][col] == "V":
            total_nice += 1

nice_kids = total_nice
delivered = 0

command = input()
while command != "Christmas morning":
    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = get_new_pos(santa_row, santa_col, command)

    if matrix[santa_row][santa_col] == "V":
        num_presents -= 1
        nice_kids -= 1
        delivered += 1

    if matrix[santa_row][santa_col] == "C":

        if matrix[santa_row - 1][santa_col] == "V" and num_presents:
            num_presents -= 1
            nice_kids -= 1
            delivered += 1
            matrix[santa_row - 1][santa_col] = "-"
        elif matrix[santa_row - 1][santa_col] == "X" and num_presents:
            num_presents -= 1
            matrix[santa_row - 1][santa_col] = "-"

        if matrix[santa_row][santa_col + 1] == "V" and num_presents:
            num_presents -= 1
            nice_kids -= 1
            delivered += 1
            matrix[santa_row][santa_col + 1] = "-"
        elif matrix[santa_row][santa_col + 1] == "X" and num_presents:
            num_presents -= 1
            matrix[santa_row][santa_col + 1] = "-"

        if matrix[santa_row + 1][santa_col] == "V" and num_presents:
            num_presents -= 1
            nice_kids -= 1
            delivered += 1
            matrix[santa_row + 1][santa_col] = "-"
        elif matrix[santa_row + 1][santa_col] == "X" and num_presents:
            num_presents -= 1
            matrix[santa_row + 1][santa_col] = "-"

        if matrix[santa_row][santa_col - 1] == "V" and num_presents:
            num_presents -= 1
            nice_kids -= 1
            delivered += 1
            matrix[santa_row][santa_col - 1] = "-"
        elif matrix[santa_row][santa_col - 1] == "X" and num_presents:
            num_presents -= 1
            matrix[santa_row][santa_col - 1] = "-"

    matrix[santa_row][santa_col] = "S"

    if nice_kids == 0 or num_presents == 0:
        break

    command = input()

if num_presents == 0 and delivered < total_nice:
    print(f"Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if delivered == total_nice:
    print(f"Good job, Santa! {total_nice} happy nice kid/s.")
else:
    print(f"No presents for {total_nice - delivered} nice kid/s.")
