cats_count = int(input())

group1 = 0
group2 = 0
group3 = 0
grams = 0
money = 0

for cat in range(1, cats_count + 1):
    cat_food = float(input())
    if 100 <= cat_food < 200:
        group1 += 1
        grams += cat_food
    elif 200 <= cat_food < 300:
        group2 += 1
        grams += cat_food
    elif 300 <= cat_food < 400:
        group3 += 1
        grams += cat_food

money = (grams / 1000) * 12.45

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {money:.2f} lv.")
