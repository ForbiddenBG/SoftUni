def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols

rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    line = input()
    if line == "END":
        break

    command_args = line.split()

    if len(command_args) != 5 or command_args[0] != "swap":
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in command_args[1:]]

    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=' ')


# def is_inside(row1, col1, row2, col2, r_u, c_u):
#     if 0 <= row1 < r_u and 0 <= col1 < c_u and 0 <= row2 < r_u and 0 <= col2 < c_u:
#         return True
#     return False
#
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for _ in range(rows):
#     nums = [x for x in input().split()]
#     matrix.append(nums)
#
# command = input()
# while command != "END":
#     main_data = command.split()
#     if len(main_data) == 5:
#         r1, c1, r2, c2 = [int(x) for x in main_data[1:]]
#         valid = is_inside(r1, c1, r2, c2, rows, cols)
#         if main_data[0] == "swap" and valid:
#             matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
#             for row in matrix:
#                 print(*row, sep=" ")
#         else:
#             print("Invalid input!")
#     else:
#         print("Invalid input!")
#     command = input()
