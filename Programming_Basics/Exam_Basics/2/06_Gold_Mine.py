locations_count = int(input())

gold_for_all_days_per_location = 0

for location in range(1, locations_count + 1):
    expected_half_amount_per_day = float(input())
    number_of_days_per_location = int(input())
    for day in range(1, number_of_days_per_location + 1):
        gold_for_the_day = float(input())
        gold_for_all_days_per_location += gold_for_the_day
    half_amount_per_day = gold_for_all_days_per_location / number_of_days_per_location
    if half_amount_per_day >= expected_half_amount_per_day:
        print(f"Good job! Average gold per day: {half_amount_per_day:.2f}.")
    else:
        print(f"You need {abs(expected_half_amount_per_day - half_amount_per_day):.2f} gold.")
    gold_for_all_days_per_location = 0
