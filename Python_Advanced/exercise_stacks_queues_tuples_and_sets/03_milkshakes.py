from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and cups and milkshakes < 5:
    last_chocolate = chocolates.pop()
    first_cup = cups.popleft()
    if last_chocolate <= 0 and first_cup <= 0:
        continue
    if last_chocolate <= 0:
        cups.appendleft(first_cup)
        continue
    if first_cup <= 0:
        chocolates.append(last_chocolate)
        continue
    if last_chocolate == first_cup:
        milkshakes += 1
    else:
        chocolates.append(last_chocolate - 5)
        cups.append(first_cup)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups:
    print(f"Milk: {', '.join(str(x) for x in cups)}")
else:
    print("Milk: empty")
