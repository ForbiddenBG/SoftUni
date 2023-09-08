def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbours(row, col, matrix):
    size = len(matrix)
    neighbours = []

    # row - 1, col
    if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
        neighbours.append([row - 1, col])
    # row + 1, col
    if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighbours.append([row + 1, col])
    # row, col - 1
    if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
        neighbours.append([row, col - 1])
    # row, col + 1
    if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
        neighbours.append([row, col + 1])
    # row - 1, col - 1
    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neighbours.append([row - 1, col - 1])
    # row - 1, col + 1
    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neighbours.append([row - 1, col + 1])
    # row + 1, col - 1
    if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neighbours.append([row + 1, col - 1])
    # row + 1, col + 1
    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighbours.append([row + 1, col + 1])
    return neighbours


n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb_coords in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb_coords.split(',')]

    if matrix[bomb_row][bomb_col] <= 0:
        continue

    bomb_power = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0

    for row, col in get_neighbours(bomb_row, bomb_col, matrix):
        matrix[row][col] -= bomb_power

alive_cells = 0
alive_cells_sum = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_cells_sum += el

print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_cells_sum}')

for row in matrix:
    print(*row, sep=' ')

# def is_inside(r, c, size):
#     return 0 <= r < size and 0 <= c < size
#
#
# def explosions(r, c, value):
#     size = len(matrix)
#     if is_inside(r-1, c-1, size) and matrix[r-1][c-1] > 0:
#         matrix[r-1][c-1] -= value
#     if is_inside(r-1, c, size) and matrix[r-1][c] > 0:
#         matrix[r-1][c] -= value
#     if is_inside(r-1, c+1, size) and matrix[r-1][c+1] > 0:
#         matrix[r-1][c+1] -= value
#     if is_inside(r, c-1, size) and matrix[r][c-1] > 0:
#         matrix[r][c-1] -= value
#     if is_inside(r, c+1, size) and matrix[r][c+1] > 0:
#         matrix[r][c+1] -= value
#     if is_inside(r+1, c-1, size) and matrix[r+1][c-1] > 0:
#         matrix[r+1][c-1] -= value
#     if is_inside(r+1, c, size) and matrix[r+1][c] > 0:
#         matrix[r+1][c] -= value
#     if is_inside(r+1, c+1, size) and matrix[r+1][c+1] > 0:
#         matrix[r+1][c+1] -= value
#
#
# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     nums = [int(x) for x in input().split()]
#     matrix.append(nums)
#
# indexes = input().split()
#
# for bomb in indexes:
#     bomb_row, bomb_col = [int(x) for x in bomb.split(",")]
#     if is_inside(bomb_row, bomb_col, len(matrix)) and matrix[bomb_row][bomb_col] > 0:
#         explosions(bomb_row, bomb_col, matrix[bomb_row][bomb_col])
#         matrix[bomb_row][bomb_col] = 0
#
# alive_cells = 0
# alive_cells_sum = 0
# for row in range(n):
#     for col in range(len(matrix[row])):
#         if matrix[row][col] > 0:
#             alive_cells += 1
#             alive_cells_sum += matrix[row][col]
#
# print(f"Alive cells: {alive_cells}")
# print(f"Sum: {alive_cells_sum}")
#
# for row in matrix:
#     print(*row, sep=" ")
