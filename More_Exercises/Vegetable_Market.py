price_per_kg_veges = float(input())
price_per_kg_fruit = float(input())
total_kg_veges = int(input())
total_kg_fruit = int(input())

euro = 1.94

total_money = total_kg_veges * price_per_kg_veges + total_kg_fruit * price_per_kg_fruit
money_in_euro = total_money / 1.94

print(f"{money_in_euro:.2f}")