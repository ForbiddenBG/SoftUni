minutes_walk_per_day = int(input())
number_of_walks_daily = int(input())
calories_daily = int(input())

total_minutes_walk = minutes_walk_per_day * number_of_walks_daily
total_burned_calories = total_minutes_walk * 5

if total_burned_calories >= calories_daily / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
elif total_burned_calories <calories_daily / 2:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")
