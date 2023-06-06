number = int(input())

binary_number = int(input())

count = 0

while number > 0:
    leftover = number % 2
    if leftover == binary_number:
        count += 1

    number //= 2

print(count)
