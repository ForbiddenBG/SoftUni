heroes = {}

command = input()
while not command == "End":
    main_data = command.split()
    if main_data[0] == "Enroll":
        hero_name = main_data[1]
        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif main_data[0] == "Learn":
        hero_name, spell_name = main_data[1:]
        if hero_name in heroes:
            if spell_name not in heroes[hero_name]:
                heroes[hero_name].append(spell_name)
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")
    elif main_data[0] == "Unlearn":
        hero_name, spell_name = main_data[1:]
        if hero_name in heroes:
            if spell_name in heroes[hero_name]:
                heroes[hero_name].remove(spell_name)
            elif spell_name not in heroes[hero_name]:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")
    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda kvp: (-len(kvp[0][1]), kvp[0]))

print("Heroes:")
for key, value in sorted_heroes:
    print(f"== {key}: {', '.join(value)}")
