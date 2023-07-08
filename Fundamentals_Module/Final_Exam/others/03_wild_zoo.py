animals = {}
hungry = {}

command = input()
while not command == "EndDay":
    main_data = command.split(": ")
    if main_data[0] == "Add":
        animal, food, area = main_data[1].split("-")
        food = int(food)
        if animal not in animals:
            animals[animal] = {'food': food, 'area': area}
            if area not in hungry:
                hungry[area] = []
                hungry[area].append(animal)
            else:
                hungry[area].append(animal)
        else:
            animals[animal]['food'] += food
    elif main_data[0] == "Feed":
        animal, food = main_data[1].split("-")
        food = int(food)
        if animal in animals:
            animals[animal]['food'] -= food
            if animals[animal]['food'] <= 0:
                area = animals[animal]['area']
                hungry[area].remove(animal)
                if not hungry[area]:
                    del hungry[area]
                del animals[animal]
                print(f"{animal} was successfully fed")
    command = input()

sorted_animals = sorted(animals.items(), key=lambda kvp: (-kvp[1]['food'], kvp[0]))

print("Animals:")
for k, v in sorted_animals:
    print(f" {k} -> {v['food']}g")
print(f"Areas with hungry animals:")
for key, value in sorted(hungry.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    print(f" {key}: {len(value)}")
