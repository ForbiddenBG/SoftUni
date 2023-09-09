size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break
    command_args = line.split()

    command = command_args[0]
    row, col, value = [int(x) for x in command_args[1:]]

    if row < 0 or col < 0 or row >= size or col >= size:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")

# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# commands = input()
# while commands != "END":
#     main_data = commands.split()
#     row = int(main_data[1])
#     col = int(main_data[2])
#     value = int(main_data[3])
#     if 0 <= row < len(matrix) and 0 <= col < len(matrix):
#         if main_data[0] == "Add":
#             matrix[row][col] += value
#         elif main_data[0] == "Subtract":
#             matrix[row][col] -= value
#     else:
#         print("Invalid coordinates")
#     commands = input()
#
# for row in matrix:
#     print(*row, sep=" ")
