likes = {}
unlike_counter = 0

command = input()
while not command == "Stop":
    main_data = command.split("-")
    if main_data[0] == "Like":
        guest, meal = main_data[1:]
        if guest not in likes:
            likes[guest] = []
            likes[guest].append(meal)
        else:
            likes[guest].append(meal)
    elif main_data[0] == "Dislike":
        guest, meal = main_data[1:]
        if guest in likes:
            if meal in likes[guest]:
                likes[guest].remove(meal)
                unlike_counter += 1
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")
    command = input()

sorted_meals = sorted(likes.items(), key=lambda kvp: kvp[0][1], reverse=True)

for k, v in sorted_meals:
    print(f"{k}: {', '.join([el for el in v])}")
print(f"Unliked meals: {unlike_counter}")
