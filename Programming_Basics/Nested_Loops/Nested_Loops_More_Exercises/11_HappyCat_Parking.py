days_count = int(input())
hours_count = int(input())

tax = 0.0

for day in range(1, days_count + 1):
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and hour % 2 == 1:
            tax += 2.50

        elif day % 2 == 1 and hour % 2 == 0:
            tax += 1.25

        else:
            tax += 1

        print(f"Day: {day} – {tax} leva")




print(f"Total: {tax} leva")
