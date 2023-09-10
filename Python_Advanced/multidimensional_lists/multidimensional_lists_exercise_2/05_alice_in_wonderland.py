def is_inside(r, c, s):
    return 0 <= r < len(s) and 0 <= c < len(s)


def get_next_pos(r, c, comm):
    if comm == "up":
        return r-1, c
    if comm == "down":
        return r+1, c
    if comm == "right":
        return r, c+1
    if comm == "left":
        return r, c-1


size = int(input())

matrix = []

alice_row, alice_col = 0, 0

for row in range(size):
    matrix.append([x for x in input().split()])
    for col in range(size):
        if matrix[row][col] == "A":
            alice_row, alice_col = row, col

tea_bags = 0

matrix[alice_row][alice_col] = "*"
command = input()
while True:
    alice_row, alice_col = get_next_pos(alice_row, alice_col, command)
    if is_inside(alice_row, alice_col, matrix):
        if matrix[alice_row][alice_col] == "R" and tea_bags < 10:
            matrix[alice_row][alice_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        if matrix[alice_row][alice_col].isdigit():
            tea_bags += int(matrix[alice_row][alice_col])
            matrix[alice_row][alice_col] = "*"
        if tea_bags >= 10:
            print("She did it! She went to the party.")
            break
        matrix[alice_row][alice_col] = "*"
    else:
        print("Alice didn't make it to the tea party.")
        break
    command = input()

for row in matrix:
    print(*row)
