luggage_over_20_cost = float(input())
luggage_kg = float(input())
day_to_the_trip = int(input())
luggage_count = int(input())

luggage_tax = 0

if luggage_kg <= 10:
    luggage_tax = luggage_over_20_cost - (luggage_over_20_cost * 0.20)
elif 10 < luggage_kg <= 20:
    luggage_tax = luggage_over_20_cost / 2
elif 20 < luggage_kg:
    luggage_tax = float(luggage_over_20_cost)

if day_to_the_trip < 7:
    luggage_tax += luggage_tax * 0.40
elif 7 < day_to_the_trip <= 30:
    luggage_tax = luggage_tax * 0.15
else:
    luggage_tax += luggage_tax * 0.10

total = luggage_tax * luggage_count

print(f"The total price of bags is: {total:.2f} lv.")

