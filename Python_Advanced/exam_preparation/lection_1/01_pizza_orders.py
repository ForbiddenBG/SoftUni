from collections import deque


def process_pizzas(pizzas, employees):
    total_pizzas_count = 0
    while pizzas and employees:
        while pizzas[0] > employees[-1]:
            total_pizzas_count += employees[-1]
            pizzas[0] = pizzas[0] - employees[-1]
            employees.pop()

            if not pizzas or not employees:
                return total_pizzas_count

        total_pizzas_count += pizzas.popleft()
        employees.pop()
    return total_pizzas_count


pizzas = deque([int(el) for el in input().split(", ") if 0 < int(el) < 11])
employees = [int(el) for el in input().split(", ")]

total_pizzas_count = process_pizzas(pizzas, employees)

if pizzas:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in pizzas])}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_count}")
    print(f"Employees: {', '.join([str(el) for el in employees])}")