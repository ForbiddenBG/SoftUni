def is_knight(row, col, matrix):
    return matrix[row][col] == "K"


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_attack_counter(row, col, matrix):
    result = 0
    if is_inside(row - 2, col - 1, len(matrix)) and is_knight(row - 2, col - 1, matrix):
        result += 1
    if is_inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
        result += 1
    if is_inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
        result += 1
    if is_inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result += 1
    if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result += 1
    if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
        result += 1
    if is_inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
        result += 1
    if is_inside(row + 1, col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
        result += 1
    return result


size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    table = {}

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "0":
                continue
            counter = get_attack_counter(row, col, matrix)
            if counter:
                table[(row, col)] = counter

    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for coords, counter in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = coords[0]
            knight_col = coords[1]

    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)


# def is_inside(r, c, m):
#     return 0 <= r < m and 0 <= c < m
#
#
# def get_new_pos(r, c, s):
#     result = 0
#     if is_inside(r-2, c-1, len(s)) and s[r-2][c-1] == "K":
#         result += 1
#     if is_inside(r-2, c+1, len(s)) and s[r-2][c+1] == "K":
#         result += 1
#     if is_inside(r-1, c+2, len(s)) and s[r-1][c+2] == "K":
#         result += 1
#     if is_inside(r+1, c+2, len(s)) and s[r+1][c+2] == "K":
#         result += 1
#     if is_inside(r+2, c+1, len(s)) and s[r+2][c+1] == "K":
#         result += 1
#     if is_inside(r+2, c-1, len(s)) and s[r+2][c-1] == "K":
#         result += 1
#     if is_inside(r+1, c-2, len(s)) and s[r+1][c-2] == "K":
#         result += 1
#     if is_inside(r-1, c-2, len(s)) and s[r-1][c-2] == "K":
#         result += 1
#     return result
#
#
# size = int(input())
#
# matrix = []
#
# for _ in range(size):
#     matrix.append([x for x in input()])
#
# removed = 0
#
# while True:
#     matches = {}
#     for row_index in range(size):
#         for col_index in range(size):
#             if matrix[row_index][col_index] == "K":
#                 attack = get_new_pos(row_index, col_index, matrix)
#                 if attack:
#                     matches[(row_index, col_index)] = attack
#             else:
#                 continue
#
#     if len(matches) == 0:
#         break
#
#     counter = 0
#     knight_row, knight_col = 0, 0
#     for coords, attack in matches.items():
#         if attack > counter:
#             counter = attack
#             knight_row = coords[0]
#             knight_col = coords[1]
#
#     matrix[knight_row][knight_col] = "0"
#     removed += 1
#
# print(removed)
