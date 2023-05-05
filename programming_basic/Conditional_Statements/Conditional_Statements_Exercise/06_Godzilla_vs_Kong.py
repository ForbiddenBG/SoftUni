budget = float(input())
stuntmen_count = int(input())
price_per_clothing = float(input())

decor_price = budget * 0.1
total_clothing_price = price_per_clothing * stuntmen_count

if stuntmen_count > 150:
    total_clothing_price -= total_clothing_price * 0.1
    # total_clothing_price *= 0.9

money_needed = decor_price + total_clothing_price

if money_needed > budget:
    print("Not enough money!")
    print(f"Wingard needs {money_needed-budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget-money_needed:.2f} leva left.")