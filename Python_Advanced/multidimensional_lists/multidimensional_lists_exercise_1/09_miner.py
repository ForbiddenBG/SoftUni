def get_next_pos(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'down':
        return row + 1, col


n = int(input())
commands = input().split()

matrix = []

miner_row = 0
miner_col = 0
total_coal = 0

for row in range(n):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(n):
        element = row_elements[col]
        if element == 's':
            miner_row = row
            miner_col = col
        elif element == 'c':
            total_coal += 1

game_over = False
for command in commands:
    next_row, next_col = get_next_pos(command, miner_row, miner_col)

    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        continue

    miner_row, miner_col = next_row, next_col
    if matrix[miner_row][miner_col] == 'c':
        matrix[miner_row][miner_col] = '*'
        total_coal -= 1

        if total_coal == 0:
            break
    elif matrix[miner_row][miner_col] == 'e':
        game_over = True
        break

if total_coal == 0:
    print(f'You collected all coal! ({miner_row}, {miner_col})')
elif game_over:
    print(f'Game over! ({miner_row}, {miner_col})')
else:
    print(f'{total_coal} pieces of coal left. ({miner_row}, {miner_col})')

# def is_inside(r, c, size):
#     return 0 <= r < size and 0 <= c < size
#
#
# def next_move(r, c, value):
#     if value == "up":
#         return r-1, c
#     elif value == "down":
#         return r+1, c
#     elif value == "left":
#         return r, c-1
#     elif value == "right":
#         return r, c+1
#
#
# n = int(input())
#
# matrix = []
#
# commands = input().split()
#
# miner_row = 0
# miner_col = 0
# total_coal = 0
#
# for row_index in range(n):
#     string = input().split()
#     matrix.append(string)
#     for col_index in range(n):
#         if matrix[row_index][col_index] == "s":
#             miner_row = row_index
#             miner_col = col_index
#         elif matrix[row_index][col_index] == "c":
#             total_coal += 1
#
# is_not_finish = True
#
# for command in commands:
#     next_row, next_col = next_move(miner_row, miner_col, command)
#     if is_inside(next_row, next_col, n):
#         miner_row = next_row
#         miner_col = next_col
#         if matrix[next_row][next_col] == "c":
#             total_coal -= 1
#             matrix[next_row][next_col] = "*"
#             if total_coal == 0:
#                 is_not_finish = False
#                 print(f"You collected all coal! ({miner_row}, {miner_col})")
#                 break
#         elif matrix[next_row][next_col] == "e":
#             is_not_finish = False
#             print(f"Game over! ({miner_row}, {miner_col})")
#             break
#
# if is_not_finish:
#     print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_col})")
