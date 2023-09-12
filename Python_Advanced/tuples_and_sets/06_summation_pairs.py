from collections import deque

string = deque([int(x) for x in input().split()])
target_number = int(input())

equals = set()
iterations_count = 0

while string:
    first_digit = string.popleft()
    for x in string:
        iterations_count += 1
        if first_digit + x == target_number:
            equals.add((first_digit, x))
            print(f"{first_digit} + {x} = {target_number}")

print(f"Iterations done: {iterations_count}")
if equals:
    print(*equals, sep='\n')
