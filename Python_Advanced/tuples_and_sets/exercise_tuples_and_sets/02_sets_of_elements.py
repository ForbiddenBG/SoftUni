n, m = (int(i) for i in input().split())

first = set()
second = set()

for _ in range(n):
    first.add(input())

for _ in range(m):
    second.add(input())

print(*first.intersection(second), sep='\n')
