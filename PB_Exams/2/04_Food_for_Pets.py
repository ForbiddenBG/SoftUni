import math
days_count = int(input())
total_food_count = float(input())

total_food_count = input(total_food_count)
daily_eaten_food = 0
biscuits = 0
dog_food = 0
cat_food = 0

for days in range(1, days_count + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())
    dog_food += food_eaten_by_dog
    cat_food += food_eaten_by_cat
    daily_eaten_food = food_eaten_by_dog + food_eaten_by_cat
    total_food_count -= (food_eaten_by_dog + food_eaten_by_cat)
    if days % 2 != 0:
        biscuits = daily_eaten_food - (daily_eaten_food * 0.10)

print(f"Total eaten biscuits: {round(biscuits)}gr.")
percent_eaten_food = daily_eaten_food / 100
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
percent_dog_food = dog_food / 100
print(f"{percent_dog_food:.2f}% eaten from the dog.")
percent_cat_food = cat_food / 100
print(f"{percent_cat_food:.2f}% eaten from the cat.")

