number = int(input())

plant_types = {}

for _ in range(number):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    plant_types[plant] = {'Rarity': rarity, 'Rating': []}

command = input()
while not command == "Exhibition":
    operation = command.split(": ")
    if operation[0] == "Rate":
        plant, rating = operation[1].split(" - ")
        rating = int(rating)
        if plant in plant_types:
            plant_types[plant]['Rating'].append(rating)
        else:
            print("error")
    elif operation[0] == "Update":
        plant, new_rarity = operation[1].split(" - ")
        new_rarity = int(new_rarity)
        if plant in plant_types:
            plant_types[plant]['Rarity'] = new_rarity
        else:
            print("error")
    elif operation[0] == "Reset":
        plant = operation[1]
        if plant in plant_types:
            plant_types[plant]['Rating'].clear()
        else:
            print("error")
    else:
        print("error")

    command = input()

for key, value in plant_types.items():
    if value['Rating']:
        average = sum(value['Rating']) / len(value['Rating'])
    else:
        average = 0
    plant_types[key]['average'] = average

sorted_plants = sorted(plant_types.items(), key=lambda kvp: (-kvp[1]['Rarity'], kvp[1]['average']))

print("Plants for the exhibition:")
for k, v in sorted_plants:
    print(f"- {k}; Rarity: {v['Rarity']}; Rating: {v['average']:.2f}")
