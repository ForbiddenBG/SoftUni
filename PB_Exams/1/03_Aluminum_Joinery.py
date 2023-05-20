joinery_count = int(input())
joinery_type = input()
delivery = input()

total_price = 0
discount_price = 0

if joinery_count < 10:
    print(f"Invalid order")
elif joinery_type == "90X130":
    if 60 >= joinery_count > 30:
        total_price = joinery_count * 110
        discount_price = total_price - (total_price * 0.05)
    elif joinery_count > 60:
        total_price = joinery_count * 110
        discount_price = total_price - (total_price * 0.08)
    elif 30 > joinery_count > 10:
        total_price = joinery_count * 110
        discount_price = total_price
elif joinery_type == "100X150":
    if 80 >= joinery_count > 40:
        total_price = joinery_count * 140
        discount_price = total_price - (total_price * 0.06)
    elif joinery_count > 80:
        total_price = joinery_count * 140
        discount_price = total_price - (total_price * 0.10)
elif joinery_type == "130X180":
    if 50 >= joinery_count > 20:
        total_price = joinery_count * 190
        discount_price = total_price - (total_price * 0.07)
    elif joinery_count > 50:
        total_price = joinery_count * 190
        discount_price = total_price - (total_price * 0.12)
elif joinery_type == "200X300":
    if 50 >= joinery_count > 25:
        total_price = joinery_count * 250
        discount_price = total_price - (total_price * 0.09)
    elif joinery_count > 50:
        total_price = joinery_count * 250
        discount_price = total_price - (total_price * 0.14)

if delivery == "With delivery":
    discount_price += 60
    print(f"{discount_price:.2f} BGN")
if joinery_count > 99:
    discount_price += 60
    discount_price = discount_price - (discount_price * 0.04)
    print(f"{discount_price:.2f} BGN")


