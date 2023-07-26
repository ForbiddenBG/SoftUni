pirate_ship_status = input().split(">")
warship_status = input().split(">")
max_health_capacity = int(input())
is_stalemate = True

command = input()
while not command == "Retire":
    data = command.split()
    if data[0] == "Fire":
        index = int(data[1])
        dmg = int(data[2])
        if index in range(len(warship_status)):
            status = int(warship_status[index])
            if status - dmg > 0:
                status -= dmg
                warship_status.pop(index)
                warship_status.insert(index, str(status))
            else:
                print("You won! The enemy ship has sunken.")
                is_stalemate = False
                break
        else:
            pass
    if data[0] == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        dmg = int(data[3])
        if start_index in range(len(pirate_ship_status)) and end_index in range(len(pirate_ship_status)):
            for section in range(start_index, end_index + 1):
                section_status = int(pirate_ship_status[section])
                if section_status - dmg > 0:
                    section_status -= dmg
                    pirate_ship_status.pop(section)
                    pirate_ship_status.insert(section, str(section_status))
                else:
                    print("You lost! The pirate ship has sunken.")
                    is_stalemate = False
                    break
        else:
            pass
    if data[0] == "Repair":
        index = int(data[1])
        health = int(data[2])
        if index in range(len(pirate_ship_status)):
            status = int(pirate_ship_status[index])
            if status + health < max_health_capacity:
                status += health
                pirate_ship_status.pop(index)
                pirate_ship_status.insert(index, str(status))
            else:
                status = max_health_capacity
                pirate_ship_status.pop(index)
                pirate_ship_status.insert(index, str(status))
        else:
            pass
    if data[0] == "Status":
        needed_repair = 0
        for section in range(len(pirate_ship_status)):
            section_status = int(pirate_ship_status[section])
            if section_status < (max_health_capacity * 0.2):
                needed_repair += 1
        print(f"{needed_repair} sections need repair.")
    command = input()

total_pirates = 0
for pirate in range(len(pirate_ship_status)):
    number = int(pirate_ship_status[pirate])
    total_pirates += number

total_warship = 0
for man in range(len(warship_status)):
    number = int(warship_status[man])
    total_warship += number

if is_stalemate:
    print(f"Pirate ship status: {total_pirates}")
    print(f"Warship status: {total_warship}")
