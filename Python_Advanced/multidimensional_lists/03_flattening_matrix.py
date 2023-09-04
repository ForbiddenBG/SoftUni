n = int(input())

matrix = []

for _ in range(n):
    data = [int(x) for x in input().split(", ")]
    matrix.extend(data)
    # matrix.append(data)
#
# result = []
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         result.append(matrix[row_index][col_index])
#
# print(result)
print(matrix)
