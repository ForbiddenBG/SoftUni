def is_inside(r, c, ma):
    return 0 <= r < len(ma) and 0 <= c < len(ma)


def calc_sum(ro, co, mat, mult):
    return (int(mat[0][co]) + int(mat[ro][7-1]) + int(mat[7-1][co]) + int(mat[ro][0])) * mult


player_one, player_two = input().split(", ")

size = 7

matrix = []

for _ in range(size):
    matrix.append(input().split())

counter = 0
player_one_score = 501
player_one_throw = 0
player_two_score = 501
player_two_throw = 0

command = input()
while True:
    row, col = eval(command)
    if not is_inside(row, col, matrix):
        if counter % 2 == 0:
            counter += 1
            player_one_throw += 1
            command = input()
            continue
        else:
            counter += 1
            player_two_throw += 1
            command = input()
            continue
    if is_inside(row, col, matrix):
        if counter % 2 == 0:
            counter += 1
            player_one_throw += 1
            if matrix[row][col].isdigit():
                player_one_score -= int(matrix[row][col])
            if matrix[row][col] == "D":
                multiplier = 2
                result_calc = calc_sum(row, col, matrix, multiplier)
                player_one_score -= result_calc
            if matrix[row][col] == "T":
                multiplier = 3
                result_calc = calc_sum(row, col, matrix, multiplier)
                player_one_score -= result_calc
            if matrix[row][col] == "B" or player_one_score <= 0:
                print(f"{player_one} won the game with {player_one_throw} throws!")
                break
        else:
            counter += 1
            player_two_throw += 1
            if matrix[row][col].isdigit():
                player_two_score -= int(matrix[row][col])
            if matrix[row][col] == "D":
                multiplier = 2
                result_calc = calc_sum(row, col, matrix, multiplier)
                player_two_score -= result_calc
            if matrix[row][col] == "T":
                multiplier = 3
                result_calc = calc_sum(row, col, matrix, multiplier)
                player_two_score -= result_calc
            if matrix[row][col] == "B" or player_two_score <= 0:
                print(f"{player_two} won the game with {player_two_throw} throws!")
                break
    command = input()
