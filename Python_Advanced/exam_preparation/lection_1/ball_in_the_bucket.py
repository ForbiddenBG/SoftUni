n = 6
throws_count = 3

matrix = [input().split() for _ in range(n)]
total_points = 0

for _ in range(throws_count):
    row, col = [int(el) for el in eval(input())]

    try:
        if matrix[row][col] == "B":
            total_points += sum(
                [int(matrix[row_index][col]) for row_index in range(n) if matrix[row_index][col].isdigit()])
            matrix[row][col] = '0'
    except IndexError:
        continue

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
elif 100 <= total_points < 200:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 200 <= total_points < 300:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
