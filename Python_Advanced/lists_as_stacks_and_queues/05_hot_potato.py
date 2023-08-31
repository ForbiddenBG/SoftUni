from collections import deque

names = deque(input().split())
n = int(input())

while len(names) > 1:
    names.rotate(-n)
    print(f"Removed {names.pop()}")

print(f"Last is {names.popleft()}")

# from collections import deque
#
# names = deque(input().split(" "))
# toss = int(input())
#
# while names:
#     names.rotate(-toss)
#     if len(names) > 1:
#         print(f"Removed {names.pop()}")
#     else:
#         print(f"Last is {names.pop()}")
