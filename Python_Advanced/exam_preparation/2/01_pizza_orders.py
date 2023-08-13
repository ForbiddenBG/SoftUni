from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]

total_pizzas = 0

while pizza_orders and employees:
    first_order = pizza_orders.popleft()
    if first_order > 10:
        continue
    if first_order <= 0:
        continue
    last_employee = employees.pop()
    if first_order < last_employee:
        total_pizzas += first_order
    if first_order > last_employee:
        first_order -= last_employee
        total_pizzas += last_employee
        pizza_orders.appendleft(first_order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
if employees:
    print(f"Employees: {', '.join([str(x) for x in employees])}")

# from collections import deque
#
# orders = deque([int(x) for x in input().split(", ")])
# employees = [int(x) for x in input().split(", ")]
#
# total_pizzas = 0
#
# while orders and employees:
#     pizzas = orders.popleft()
#     if 0 < pizzas <= 10:
#         worker = employees[-1]
#         if pizzas <= worker:
#             employees.pop()
#             total_pizzas += pizzas
#         elif pizzas > worker:
#             rest = pizzas - worker
#             if len(employees) > 0:
#                 total_pizzas += worker
#             orders.appendleft(rest)
#             employees.pop()
#
# if not orders:
#     print("All orders are successfully completed!")
#     print(f"Total pizzas made: {total_pizzas}")
#     print(f"Employees: {', '.join([str(x) for x in employees])}")
# elif not employees and orders:
#     print("Not all orders are completed.")
#     print(f"Orders left: {', '.join([str(x) for x in orders])}")
