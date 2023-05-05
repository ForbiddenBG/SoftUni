from math import floor

record = float(input())
distance = float(input()) #distance // 15
second_per_meter = float(input())

delay = floor((distance // 15)) * 12.5
personal_time = distance * second_per_meter + delay

if personal_time < record:
    print(f"Yes, he succeeded! The new world record is {personal_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record - personal_time):.2f} seconds slower.")