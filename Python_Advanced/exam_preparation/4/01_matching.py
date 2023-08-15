from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

counter = 0

while males and females:
    last_male = males[-1]
    first_female = females[0]
    if last_male <= 0:
        males.pop()
        continue
    if first_female <= 0:
        females.popleft()
        continue
    if last_male % 25 == 0:
        males.pop()
        males.pop()
        continue
    if first_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if last_male == first_female:
        counter += 1
        males.pop()
        females.popleft()
        continue
    females.popleft()
    males[-1] -= 2

print(f"Matches: {counter}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join([str(x) for x in reversed(males)])}")
if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(x) for x in females])}")
