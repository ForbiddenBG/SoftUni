day = input()
age = int(input())

price = 0
is_error = True

if 0 <= age <= 18:
    if day == "Weekday":
        price += 12
    elif day == "Weekend":
        price += 15
    elif day == "Holiday":
        price += 5
elif 18 < age <= 64:
    if day == "Weekday":
        price += 18
    elif day == "Weekend":
        price += 20
    elif day == "Holiday":
        price += 12
elif 64 < age <= 122:
    if day == "Weekday":
        price += 12
    elif day == "Weekend":
        price += 15
    elif day == "Holiday":
        price += 10
else:
    print("Error!")

if price > 0:
    print(f"{price}$")
