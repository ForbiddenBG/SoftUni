command = input()

cities = {}

while not command == "Sail":
    city, population, gold = command.split("||")
    population, gold = int(population), int(gold)
    if city not in cities:
        cities[city] = {'Population': population, "Gold": gold}
    else:
        cities[city]['Population'] += population
        cities[city]['Gold'] += gold
    command = input()

data = input()
while not data == "End":
    main_data = data.split("=>")

    if main_data[0] == "Plunder":
        city, people, gold = main_data[1:]
        people, gold = int(people), int(gold)
        if cities[city]['Population'] > 0 and cities[city]['Gold'] > 0:
            cities[city]['Population'] -= people
            cities[city]['Gold'] -= gold
            print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[city]['Population'] == 0 or cities[city]['Gold'] == 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    elif main_data[0] == "Prosper":
        city, gold = main_data[1:]
        gold = int(gold)
        if gold >= 0:
            cities[city]['Gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['Gold']} gold.")
        else:
            print(f"Gold added cannot be a negative number!")
    data = input()

sorted_gold = sorted(cities.items(), key=lambda kvpt: (-kvpt[1]['Gold'], kvpt[0]))

print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
if cities:
    for key, value in sorted_gold:
        print(f"{key} -> Population: {value['Population']} citizens, Gold: {value['Gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
