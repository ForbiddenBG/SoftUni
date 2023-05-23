food = int(input())

eaten = 0
rest = 0

food_eaten = input()
while food_eaten != "Adopted":
    food_eaten = int(food_eaten)
    eaten += food_eaten
    rest = (food * 1000) - eaten
    food_eaten = input()

if rest >= 0:
    print(f"Food is enough! Leftovers: {rest} grams.")
elif rest < 0:
    print(f"Food is not enough. You need {abs(rest)} grams more.")