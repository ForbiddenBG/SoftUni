budget = float(input())
type_of_ticket = input()
people_count = int(input())

transport = 0.0
money_for_tickets = 0.0

if 1 <= people_count <= 4:
    transport = budget * 0.75
elif 5 <= people_count <= 9:
    transport = budget * 0.6
elif 10 <= people_count <= 24:
    transport = budget * 0.5
elif 25 <= people_count <= 49:
    transport = budget * 0.4
else:
    transport = budget * 0.25

if type_of_ticket == "VIP":
    money_for_tickets = 499.99 * people_count
elif type_of_ticket == "Normal":
    money_for_tickets = 249.99 * people_count

money_for_rest = budget - transport

if money_for_rest >= money_for_tickets:
    money_left = money_for_rest - money_for_tickets
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = money_for_tickets - money_for_rest
    print(f"Not enough money! You need {money_needed:.2f} leva.")
