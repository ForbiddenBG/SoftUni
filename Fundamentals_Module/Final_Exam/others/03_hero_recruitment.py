collection = {}

command = input()
while not command == "End":
    main_data = command.split()
    if main_data[0] == "Enroll":
        hero_name = main_data[1]
        if hero_name not in collection:
            collection[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif main_data[0] == "Learn":
        hero_name, spell_name = main_data[1:]
        if hero_name in collection:
            if spell_name not in collection[hero_name]:
                collection[hero_name].append(spell_name)
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")
    elif main_data[0] == "Unlearn":
        hero_name, spell_name = main_data[1:]
        if hero_name in collection:
            if spell_name in collection[hero_name]:
                collection[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")
    command = input()

sorted_heroes = sorted(collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

print("Heroes:")
for key, value in sorted_heroes:
    print(f"== {key}: {', '.join(value)}")
