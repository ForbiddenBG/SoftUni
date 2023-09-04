rows, columns = [int(x) for x in input().split(", ")]

matrix = []
result = 0

for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    result += sum(nums)
    matrix.append(nums)

# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         result += matrix[row_index][col_index]

print(result)
print(matrix)
