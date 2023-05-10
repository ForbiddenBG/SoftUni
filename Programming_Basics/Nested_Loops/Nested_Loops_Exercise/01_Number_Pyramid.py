n = int(input())
current = 1

for row in range(1, n + 1):
    for position in range(1, row + 1):
        print(f"{current}", end=" ")
        current += 1

        if current > n:
            break
    if current > n:
        break
    print()