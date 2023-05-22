fruit = input()
set_size = input()
set_count = int(input())

price = 0

if set_size == "small":
    total_pieces = set_count * 2
    if fruit == "Watermelon":
        price = 56 * total_pieces
    elif fruit == "Mango":
        price = 36.66 * total_pieces
    elif fruit == "Pineapple":
        price = 42.10 * total_pieces
    elif fruit == "Raspberry":
        price = 20 * total_pieces
else:
    total_pieces = set_count * 5
    if fruit == "Watermelon":
        price = 28.70 * total_pieces
    elif fruit == "Mango":
        price = 19.60 * total_pieces
    elif fruit == "Pineapple":
        price = 24.80 * total_pieces
    elif fruit == "Raspberry":
        price = 15.20 * total_pieces

if 400 <= price <= 1000:
    price *= 0.85
elif 1000 < price:
    price *= 0.5

print(f"{price:.2f} lv.")