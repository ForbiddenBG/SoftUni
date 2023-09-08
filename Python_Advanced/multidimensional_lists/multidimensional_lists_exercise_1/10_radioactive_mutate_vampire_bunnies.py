# Решението е на лектора!

def get_next_pos(row, col, command):
    if command == 'U':
        return row - 1, col
    if command == 'L':
        return row, col - 1
    if command == 'R':
        return row, col + 1
    if command == 'D':
        return row + 1, col


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]

matrix = []
player_row = 0
player_col = 0
bunnies = set()

for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)

    for col in range(cols):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
        elif row_elements[col] == 'B':
            bunnies.add(f'{row} {col}')

won = False
dead = False

commands = input()

matrix[player_row][player_col] = '.'

for command in commands:
    next_row, next_col = get_next_pos(player_row, player_col, command)

    if is_outside(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == 'B':
        dead = True
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = next_row, next_col

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]

        if not is_outside(bunny_row - 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row - 1} {bunny_col}')
            matrix[bunny_row - 1][bunny_col] = 'B'
        if not is_outside(bunny_row + 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row + 1} {bunny_col}')
            matrix[bunny_row + 1][bunny_col] = 'B'
        if not is_outside(bunny_row, bunny_col - 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col - 1}')
            matrix[bunny_row][bunny_col - 1] = 'B'
        if not is_outside(bunny_row, bunny_col + 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col + 1}')
            matrix[bunny_row][bunny_col + 1] = 'B'

    bunnies = bunnies.union(new_bunnies)

    if matrix[player_row][player_col] == 'B':
        dead = True

    if won or dead:
        break

for row in matrix:
    print(*row, sep='')

if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')

#
# def get_next_pos(row, col, command):
#     if command == 'U':
#         return row - 1, col
#     if command == 'D':
#         return row + 1, col
#     if command == 'L':
#         return row, col - 1
#     if command == 'R':
#         return row, col + 1
#
#
# def is_outside(row, col, rows, cols):
#     return row < 0 or col < 0 or row >= rows or col >= cols
#
#
# def get_children(row, col, rows, cols):
#     possible_children = [
#         [row - 1, col],
#         [row, col - 1],
#         [row, col + 1],
#         [row + 1, col]
#     ]
#
#     result = []
#     for child_row, child_col in possible_children:
#         if not is_outside(child_row, child_col, rows, cols):
#             result.append([child_row, child_col])
#
#     return result
#
#
# rows, cols = [int(x) for x in input().split()]
#
# bunnies = set()
# player_row = 0
# player_col = 0
#
# matrix = []
#
# for row in range(rows):
#     # .....P
#     row_elements = list(input())
#     for col in range(cols):
#         if row_elements[col] == 'P':
#             player_row = row
#             player_col = col
#         elif row_elements[col] == 'B':
#             bunnies.add(f'{row} {col}')
#     matrix.append(row_elements)
#
# commands = input()
#
# won = False
# dead = False
#
# for command in commands:
#     next_row, next_col = get_next_pos(player_row, player_col, command)
#     matrix[player_row][player_col] = '.'
#
#     if is_outside(next_row, next_col, rows, cols):
#         won = True
#     elif matrix[next_row][next_col] == 'B':
#         dead = True
#         player_row, player_col = next_row, next_col
#     else:
#         matrix[next_row][next_col] = 'P'
#         player_row, player_col = next_row, next_col
#
#     new_bunnies = set()
#     for bunny in bunnies:
#         bunny_row, bunny_col = [int(x) for x in bunny.split()]
#         children = get_children(bunny_row, bunny_col, rows, cols)
#         for child_row, child_col in children:
#             new_bunnies.add(f'{child_row} {child_col}')
#             matrix[child_row][child_col] = 'B'
#             if child_row == player_row and child_col == player_col:
#                 dead = True
#
#     bunnies = bunnies.union(new_bunnies)
#
#     if won or dead:
#         break
#
# for row in matrix:
#     print(''.join(row))
#
# if won:
#     print(f'won: {player_row} {player_col}')
# else:
#     print(f'dead: {player_row} {player_col}')

# def is_inside(r, c, rr, cc):
#     return 0 <= r < rr and 0 <= c < cc
#
#
# def next_moves(r, c, value):
#     if value == "L":
#         return r, c - 1
#     elif value == "R":
#         return r, c + 1
#     elif value == "U":
#         return r - 1, c
#     elif value == "D":
#         return r + 1, c
#
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# player_row = 0
# player_col = 0
# bunnies = set()
#
# for row in range(rows):
#     string = [x for x in input()]
#     matrix.append(string)
#     for col in range(cols):
#         if matrix[row][col] == "P":
#             player_row = row
#             player_col = col
#         elif matrix[row][col] == "B":
#             bunnies.add(f"{row} {col}")
#
# won = False
# dead = False
#
# matrix[player_row][player_col] = '.'
#
# commands = input()
# for command in commands:
#     next_row, next_col = next_moves(player_row, player_col, command)
#
#     if not is_inside(next_row, next_col, rows, cols):
#         won = True
#     elif matrix[next_row][next_col] == 'B':
#         dead = True
#         player_row, player_col = next_row, next_col
#     else:
#         player_row, player_col = next_row, next_col
#
#     new_bunnies = set()
#     for bunny in bunnies:
#         bunny_row, bunny_col = [int(x) for x in bunny.split()]
#         if is_inside(bunny_row, bunny_col - 1, rows, cols):
#             matrix[bunny_row][bunny_col - 1] = "B"
#             new_bunnies.add(f"{bunny_row} {bunny_col - 1}")
#         if is_inside(bunny_row, bunny_col + 1, rows, cols):
#             matrix[bunny_row][bunny_col + 1] = "B"
#             new_bunnies.add(f"{bunny_row} {bunny_col + 1}")
#         if is_inside(bunny_row - 1, bunny_col, rows, cols):
#             matrix[bunny_row - 1][bunny_col] = "B"
#             new_bunnies.add(f"{bunny_row - 1} {bunny_col}")
#         if is_inside(bunny_row + 1, bunny_col, rows, cols):
#             matrix[bunny_row + 1][bunny_col] = "B"
#             new_bunnies.add(f"{bunny_row + 1} {bunny_col}")
#         bunnies = bunnies.union(new_bunnies)
#
#     if matrix[player_row][player_col] == 'B':
#         dead = True
#
#     if won or dead:
#         break
#
# for row in matrix:
#     print(*row, sep="")
#
# if won:
#     print(f"won: {player_row} {player_col}")
# else:
#     print(f"dead: {player_row} {player_col}")
