number = int(input())

cars = {}

for _ in range(number):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {'mileage': mileage, 'fuel': fuel}

command = input()
while not command == "Stop":
    main_data = command.split(" : ")
    if main_data[0] == "Drive":
        car, distance, fuel = main_data[1:]
        distance = int(distance)
        fuel = int(fuel)
        if cars[car]['fuel'] - fuel > 0:
            cars[car]['fuel'] -= fuel
            cars[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars[car]['mileage'] >= 100_000:
            del cars[car]
            print(f"Time to sell the {car}!")
    elif main_data[0] == "Refuel":
        car, fuel = main_data[1:]
        fuel = int(fuel)
        overfill = 0
        if cars[car]['fuel'] + fuel > 75:
            overfill = cars[car]['fuel'] - 75
            cars[car]['fuel'] = 75
            print(f"{car} refueled with {fuel - overfill} liters")
        else:
            cars[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif main_data[0] == "Revert":
        car, kilometers = main_data[1:]
        kilometers = int(kilometers)
        cars[car]['mileage'] -= kilometers
        if cars[car]['mileage'] < 10_000:
            cars[car]['mileage'] = 10_000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()

sorted_cars = sorted(cars.items(), key=lambda kvp: (-kvp[1]['mileage'], kvp[0]))

for k, v in sorted_cars:
    print(f"{k} -> Mileage: {v['mileage']} kms, Fuel in the tank: {v['fuel']} lt.")