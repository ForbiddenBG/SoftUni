flower_type = input()
flower_count = int(input())
budget = int(input())

total_price = 0
if flower_type == "Roses":
    total_price = flower_count * 5
    if flower_count > 80:
        total_price -= 0.1 * total_price

elif flower_type == "Dahlias":
    total_price = flower_count * 3.80
    if flower_count > 90:
        total_price -= 0.15 * total_price

elif flower_type == "Tulips":
    total_price = flower_count * 2.80
    if flower_count > 80:
        total_price -= 0.15 * total_price

elif flower_type == "Narcissus":
    total_price = flower_count * 3
    if flower_count < 120:
        total_price += 0.15 * total_price

elif flower_type == "Gladiolus":
    total_price = flower_count * 2.50
    if flower_count < 80:
        total_price += 0.20 * total_price

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {abs(budget - total_price):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - total_price):.2f} leva more.")