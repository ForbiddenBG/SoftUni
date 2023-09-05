rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = -99999999999999999999999999
max_sum_matrix = []

for row_index in range(rows - 1):
    for cols_index in range(cols - 1):
        sub_matrix = [matrix[row_index][cols_index], matrix[row_index][cols_index + 1],
                      matrix[row_index + 1][cols_index], matrix[row_index + 1][cols_index + 1]]

        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = sub_matrix.copy()

print(max_sum_matrix[0], max_sum_matrix[1])
print(max_sum_matrix[2], max_sum_matrix[3])
print(max_sum)

# row, col = [int(x) for x in input().split(", ")]
#
# matrix = []
#
# for _ in range(row):
#     nums = [int(x) for x in input().split(", ")]
#     matrix.append(nums)
#
# max_num = float("-inf")
#
# match = []
#
# for row_index in range(row - 1):
#     for col_index in range(col - 1):
#         sum_square = [matrix[row_index][col_index], matrix[row_index][col_index + 1],
#                       matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1]]
#
#         if sum(sum_square) > max_num:
#             max_num = sum(sum_square)
#             match = sum_square.copy()
#
# print(*match[0:2])
# print(*match[2:4])
# print(max_num)
