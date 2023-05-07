goal_for_the_day = int(input())

money = 0

command = input()
while command != "closed":
    command_type = input()
    if command == "haircut":
        if command_type == "mens":
            money += 15
        elif command_type == "ladies":
            money += 20
        elif command_type == "kids":
            money += 10
    elif command == "color":
        if command_type == "touch up":
            money += 20
        elif command_type == "full color":
            money += 30

    if money >= goal_for_the_day:
        break

    command = input()


if money >= goal_for_the_day:
    print(f"You have reached your target for the day!")
elif command == "closed":
    not_enough = money - goal_for_the_day
    print(f"Target not reached! You need {abs(not_enough)}lv. more.")

print(f"Earned money: {money}lv.")

