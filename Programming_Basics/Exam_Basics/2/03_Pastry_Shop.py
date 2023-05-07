sladkish = input()
sladkishi_count = int(input())
day_of_the_month = int(input())

price = 0

if day_of_the_month <= 15:
    if sladkish == "Cake":
        price = sladkishi_count * 24
    elif sladkish == "Souffle":
        price = sladkishi_count * 6.66
    elif sladkish == "Baklava":
        price = sladkishi_count * 12.60
elif 15 < day_of_the_month:
    if sladkish == "Cake":
        price = sladkishi_count * 28.70
    elif sladkish == "Souffle":
        price = sladkishi_count * 9.80
    elif sladkish == "Baklava":
        price = sladkishi_count * 16.98

if day_of_the_month <= 22:
    if 100 <= price <= 200:
        price = price - (price * 0.15)
    elif 200 < price:
        price = price - (price * 0.25)
    if day_of_the_month <= 15:
        price = price - (price * 0.10)

print(f"{price:.2f}")


