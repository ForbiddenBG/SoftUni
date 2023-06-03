budget = float(input())
price_for_1kg_flour = float(input())

price_of_1_pack_eggs = price_for_1kg_flour * 0.75
price_of_1l_milk = price_for_1kg_flour * price_for_1kg_flour / 4
money_needed = price_for_1kg_flour + price_of_1_pack_eggs + price_of_1l_milk

bread = 0
color_eggs = 0

while money_needed < budget:
    budget -= money_needed
    bread += 1
    color_eggs += 3
    if bread % 3 == 0:
        color_eggs -= (bread - 2)

print(f"You made {bread} loaves of Easter bread! Now you have {color_eggs} eggs and {budget:.2f}BGN left.")
