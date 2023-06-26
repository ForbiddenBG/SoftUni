people = {}
count_of_people = 0

command = input()
while not command == "Results":
    main_data = command.split(":")
    if main_data[0] == "Add":
        name, health, energy = main_data[1:]
        health = int(health)
        energy = int(energy)
        if name not in people:
            people[name] = {'health': health, 'energy': energy}
            count_of_people += 1
        else:
            people[name]['health'] += health
    elif main_data[0] == "Attack":
        attacker_name, defender_name, damage = main_data[1:]
        damage = int(damage)
        if attacker_name in people and defender_name in people:
            people[defender_name]['health'] -= damage
            people[attacker_name]['energy'] -= 1
            if people[defender_name]['health'] <= 0:
                del people[defender_name]
                count_of_people -= 1
                print(f"{defender_name} was disqualified!")
            if people[attacker_name]['energy'] == 0:
                del people[attacker_name]
                count_of_people -= 1
                print(f"{attacker_name} was disqualified!")
    elif main_data[0] == "Delete":
        username = main_data[1]
        if username in people:
            del people[username]
            count_of_people -= 1
        elif username == "All":
            people = {}
            count_of_people = 0
    command = input()

sorted_people = sorted(people.items(), key=lambda kvp: (-kvp[1]['health'], kvp[0]))

print(f"People count: {count_of_people}")
for key, value in sorted_people:
    print(f"{key} - {value['health']} - {value['energy']}")
