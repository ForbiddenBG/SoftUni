from math import ceil

budget = float(input())
students = int(input())
price_per_flour = float(input())
price_per_egg = float(input())
price_per_apron = float(input())

price = 0

aprons_count = ceil(students + students * 0.2)

for student in range(1, students + 1):
    price += price_per_egg * 10
    if not student % 5 == 0:
        price += price_per_flour

aprons_cost = aprons_count * price_per_apron

total = price + aprons_cost

if budget >= price:
    print(f"Items purchased for {total:.2f}$.")
else:
    print(f"{abs(budget - total):.2f}$ more needed.")

# from math import ceil
#
# budget = float(input())
# students = int(input())
# flour_price = float(input())
# egg_price = float(input())
# apron_price = float(input())
#
# total_flour = flour_price * students - students // 5 * flour_price
#
# total_eggs = 10 * egg_price * students
#
# total_aprons = ceil(students * 1.2) * apron_price
#
# total_sets = total_flour + total_eggs + total_aprons
#
# if budget >= total_sets:
#     print(f'Items purchased for {total_sets:.2f}$.')
# else:
#     print(f'{total_sets - budget:.2f}$ more needed.')
