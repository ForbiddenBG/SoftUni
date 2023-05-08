cargo_count = int(input())

money_micro = 0
money_tir = 0
money_train = 0
total_tons = 0
mid_price_per_ton = 0
percent_micro = 0
percent_tir = 0
percent_train = 0

for cargo in range(1, cargo_count + 1):
    tons_per_cargo = int(input())
    total_tons += int(tons_per_cargo)
    if tons_per_cargo <= 3:
        money_micro = tons_per_cargo * 200
        percent_micro = tons_per_cargo / total_tons * 100
    elif 4 <= tons_per_cargo <= 11:
        money_tir = tons_per_cargo * 175
        percent_tir = tons_per_cargo / total_tons * 100
    else:
        money_train = tons_per_cargo * 120
        percent_train = tons_per_cargo / total_tons * 100

    mid_price_per_ton = (money_micro + money_tir + money_train)/total_tons

print(f"{mid_price_per_ton:.2f}")
print(f"{percent_micro}%")
print(f"{percent_tir}%")
print(f"{percent_train}%")