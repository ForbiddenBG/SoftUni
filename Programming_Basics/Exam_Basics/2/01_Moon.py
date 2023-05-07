from math import ceil
average_speed = float(input())
fuel_for_100km = float(input())

lenght = 384400

total_lenght = lenght * 2
time_for_trip = ceil(total_lenght / average_speed)
total_time = time_for_trip + 3
fuel = (fuel_for_100km * total_lenght) / 100

fuel = int(fuel)

print(f"{ceil(total_time)}")
print(f"{fuel}")