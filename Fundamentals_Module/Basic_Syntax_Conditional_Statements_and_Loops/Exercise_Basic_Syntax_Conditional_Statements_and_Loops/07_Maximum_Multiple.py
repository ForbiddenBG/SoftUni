divisor = int(input())
bound = int(input())

n = 0

for num in range(1, bound + 1):
# for num in range(bound, 0, - 1):
    if num % divisor == 0:
        n = num

print(n)
