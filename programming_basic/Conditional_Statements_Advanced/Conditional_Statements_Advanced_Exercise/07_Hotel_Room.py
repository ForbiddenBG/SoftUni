month = input()
night_count = int(input())

studio_price = 0.0
apartment_price = 0.0

if month == "May" or month == "October":
    if 7 < night_count <= 14:
        studio_price = 0.95 * 50
    elif night_count > 14:
        studio_price = 50 * 0.7
    else:
        studio_price = 50

    if night_count > 14:
         apartment_price = 0.9 * 65
    else:
         apartment_price = 65

if month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if night_count > 14:
        studio_price *= 0.80
        apartment_price *= 0.90

if month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if night_count > 14:
        apartment_price *= 0.90

print(f"Apartment: {(apartment_price * night_count):.2f} lv.")
print(f"Studio: {(studio_price * night_count):.2f} lv.")