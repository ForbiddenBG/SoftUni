from collections import deque

quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    if quantity_of_food >= orders[0]:
        current_order = orders.popleft()
        quantity_of_food -= current_order
    else:
        break

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")
    