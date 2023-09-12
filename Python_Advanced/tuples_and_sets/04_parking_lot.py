number = int(input())

plates = set()

for _ in range(number):
    direction, car_number = input().split(", ")
    if direction == "IN":
        plates.add(car_number)
    elif direction == "OUT":
        plates.discard(car_number)

if plates:
    print(*plates, sep='\n')
else:
    print("Parking Lot is Empty")
