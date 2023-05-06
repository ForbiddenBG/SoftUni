fruit = input()
day_of_week = input()
quantity = float(input())
price = 0

is_working_day = day_of_week == "Monday" or \
    day_of_week == "Tuesday" or \
    day_of_week == "Wednesday" or \
    day_of_week == "Thursday" or \
    day_of_week == "Friday"
is_weekend = day_of_week == "Saturday" or \
    day_of_week == "Sunday"

if is_working_day:
    if fruit == "banana":
        price = 2.5
    elif fruit == "apple":
        price = 1.2
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.5
    elif fruit == "grapes":
        price = 3.85
elif is_weekend:
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.9
    elif fruit == "grapefruit":
        price = 1.6
    elif fruit == "kiwi":
        price = 3.0
    elif fruit == "pineapple":
        price = 5.6
    elif fruit == "grapes":
        price = 4.2


if price == 0:
    print("error")
else:
    final_price = price * quantity
    print(f"{final_price:.2f}")