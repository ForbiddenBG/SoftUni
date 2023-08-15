def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for i in range(2, n):
        last = triangle[-1]
        triangle.append([last[0]])

        for j in range(len(last) - 1):
            result = last[j] + last[j + 1]
            triangle[i].append(result)
        triangle[i].append(last[-1])
    return triangle


get_magic_triangle(5)
