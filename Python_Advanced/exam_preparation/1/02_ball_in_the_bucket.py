def is_inside(r, c, ro, co):
    return 0 <= r < ro and 0 <= c < co


rows = 6
cols = 6

matrix = []

for row in range(rows):
    matrix.append(input().split())

points = 0
for _ in range(3):
    row, col = eval(input())
    if is_inside(row, col, rows, cols):
        if matrix[row][col] == "B":
            matrix[row][col] = "0"
            for row in range(rows):
                points += int(matrix[row][col])


if 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")

# size = 6
#
# matrix = []
#
# for _ in range(size):
#     matrix.append(input().split())
#
# result = 0
# for _ in range(3):
#     row, col = [int(x) for x in input().strip("()").split(", ")]
#     if row < 0 or col < 0 or row >= size or col >= size:
#         continue
#     if matrix[row][col] == "B":
#         for i in range(len(matrix)):
#             if matrix[i][col].isdigit():
#                 result += int(matrix[i][col])
#         matrix[row][col] = "."
#
# if 100 <= result <= 199:
#     print(f"Good job! You scored {result} points, and you've won Football.")
# elif 200 <= result <= 299:
#     print(f"Good job! You scored {result} points, and you've won Teddy Bear.")
# elif 300 <= result:
#     print(f"Good job! You scored {result} points, and you've won Lego Construction Set.")
# else:
#     print(f"Sorry! You need {100 - result} points more to win a prize.")
