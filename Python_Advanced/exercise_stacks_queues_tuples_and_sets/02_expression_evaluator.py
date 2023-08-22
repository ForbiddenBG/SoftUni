from collections import deque

string = input().split()
numbers = deque()

for el in string:
    if el in "+-*/":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            result = 0
            if el == "+":
                result = first + second
            elif el == "-":
                result = first - second
            elif el == "*":
                result = first * second
            else:
                result = first // second
            numbers.appendleft(result)
    else:
        numbers.append(int(el))

print(numbers.popleft())
