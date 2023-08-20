def is_inside(r, c, ma):
    return 0 <= r < len(ma) and 0 <= c < len(ma)


def calc_numbers(r_idx, c_idx, matrx):
    if is_inside(r_idx-1, c_idx, matrx) and matrix[r_idx-1][c_idx] != "*":
        matrx[r_idx-1][c_idx] += 1
    if is_inside(r_idx-1, c_idx+1, matrx) and matrix[r_idx-1][c_idx + 1] != "*":
        matrx[r_idx - 1][c_idx+1] += 1
    if is_inside(r_idx, c_idx+1, matrx) and matrix[r_idx][c_idx + 1] != "*":
        matrx[r_idx][c_idx+1] += 1
    if is_inside(r_idx+1, c_idx+1, matrx) and matrix[r_idx+1][c_idx + 1] != "*":
        matrx[r_idx + 1][c_idx+1] += 1
    if is_inside(r_idx+1, c_idx, matrx) and matrix[r_idx+1][c_idx] != "*":
        matrx[r_idx + 1][c_idx] += 1
    if is_inside(r_idx+1, c_idx-1, matrx) and matrix[r_idx+1][c_idx - 1] != "*":
        matrx[r_idx + 1][c_idx-1] += 1
    if is_inside(r_idx, c_idx-1, matrx) and matrix[r_idx][c_idx - 1] != "*":
        matrx[r_idx][c_idx-1] += 1
    if is_inside(r_idx-1, c_idx-1, matrx) and matrix[r_idx-1][c_idx - 1] != "*":
        matrx[r_idx - 1][c_idx-1] += 1


size = int(input())
bombs = int(input())

matrix = []

for row in range(size):
    matrix.append([])
    for col in range(size):
        matrix[row].append(0)

for _ in range(bombs):
    row, col = eval(input())
    matrix[row][col] = "*"
    calc_numbers(row, col, matrix)

for row in matrix:
    print(*row)
