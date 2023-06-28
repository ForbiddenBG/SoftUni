people = {}
unlike_meals = 0

command = input()
while not command == "Stop":
    main_data = command.split("-")
    if main_data[0] == "Like":
        guest, meal = main_data[1:]
        if guest not in people:
            people[guest] = [meal]
        if meal not in people[guest]:
            people[guest].append(meal)
    elif main_data[0] == "Unlike":
        guest, meal = main_data[1:]
        if guest in people:
            if meal in people[guest]:
                people[guest].remove(meal)
                unlike_meals += 1
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        elif guest not in people:
            print(f"{guest} is not at the party.")
    command = input()

sorted_guests = sorted(people.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

for key, value in sorted_guests:
    print(f"{key}: {', '.join([el for el in value])}")
print(f"Unliked meals: {unlike_meals}")
