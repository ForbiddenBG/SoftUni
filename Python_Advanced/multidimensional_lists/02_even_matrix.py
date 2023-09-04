rows = int(input())

matrix = []

for _ in range(rows):
    nums = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(nums)

# matrix = [[[int(x) for x in input().split(", ") if int(x) % 2 == 0]] for _ in range(rows)]
print([*matrix])

# rows = int(input())
#
# matrix = []
#
# matrix.append([[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(rows)])
#
# print(matrix)

# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])
#
# print(matrix)

# rows = int(input())
#
# matrix = []
# sum_of_nums = 0
# even_matrix = []
#
# for _ in range(rows):
#     nums = [int(x) for x in input().split(", ")]
#     matrix.append(nums)
#
# for row_index in range(len(matrix)):
#     even_matrix.append([])
#     for col_index in range(len(matrix[row_index])):
#         if matrix[row_index][col_index] % 2 == 0:
#             even_matrix[row_index].append(matrix[row_index][col_index])
#
# print(even_matrix)
