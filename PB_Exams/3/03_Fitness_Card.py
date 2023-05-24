budget = float(input())
sex = input()
age = int(input())
sport = input()

expenses = 0

if sex == "m":
    if sport == "Gym":
        expenses += 42
    elif sport == "Boxing":
        expenses += 41
    elif sport == "Yoga":
        expenses += 45
    elif sport == "Zumba":
        expenses += 34
    elif sport == "Dances":
        expenses += 51
    elif sport == "Pilates":
        expenses += 39
elif sex == "f":
    if sport == "Gym":
        expenses += 35
    elif sport == "Boxing":
        expenses += 37
    elif sport == "Yoga":
        expenses += 42
    elif sport == "Zumba":
        expenses += 31
    elif sport == "Dances":
        expenses += 53
    elif sport == "Pilates":
        expenses += 37

if age <= 19:
    expenses = expenses - (expenses * 0.2)

if expenses <= budget:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(budget - expenses):.2f} more.")