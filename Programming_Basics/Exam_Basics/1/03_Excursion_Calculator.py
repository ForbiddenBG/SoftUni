people_count = int(input())
sezon = input()

price = 0

if people_count <= 5:
    if sezon == "spring":
        price = people_count * 50
    elif sezon == "summer":
        price = people_count * 48.50
    elif sezon == "autumn":
        price = people_count * 60
    elif sezon == "winter":
        price = people_count * 86
elif people_count > 5:
    if sezon == "spring":
        price = people_count * 48
    elif sezon == "summer":
        price = people_count * 45
    elif sezon == "autumn":
        price = people_count * 49.50
    elif sezon == "winter":
        price = people_count * 85

if sezon == "summer":
    price = price - (price * 0.15)
elif sezon == "winter":
    price = price + (price * 0.08)

print(f"{price:.2f} leva.")