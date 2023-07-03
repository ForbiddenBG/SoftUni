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

# animals = {}
# hungry_animals = {}
# command = input()
# while not command == "EndDay":
#     main_data = command.split(": ")
#     if main_data[0] == "Add":
#         name, food, area = main_data[1].split("-")
#         food = int(food)
#         if name not in animals:
#             animals[name] = {'food': food, 'area': area}
#             if area not in hungry_animals:
#                 hungry_animals[area] = [name]
#             else:
#                 hungry_animals[area].append(name)
#         else:
#             animals[name]['food'] += food
#     elif main_data[0] == "Feed":
#         name, food = main_data[1].split("-")
#         food = int(food)
#         if name in animals:
#             animals[name]['food'] -= food
#             if animals[name]['food'] <= 0:
#                 del animals[name]
#                 print(f"{name} was successfully fed")
#                 for area, value in hungry_animals.items():
#                     if name in value:
#                         hungry_animals[area].remove(name)
#         else:
#             pass
#     command = input()
#
#
# sorted_animals = sorted(animals.items(), key=lambda kvp: (-kvp[1]['food'], kvp[0]))
#
# print("Animals:")
# for k, v in sorted_animals:
#     print(f" {k} -> {v['food']}g")
#
# print("Areas with hungry animals:")
# for area, stats in sorted(hungry_animals.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
#     if len(stats) > 0:
#         print(f" {area}: {len(stats)}")
