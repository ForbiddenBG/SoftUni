import math

year_type = input()  # leap / normal
vacations_days_count = int(input())
weekends_out_count = int(input())

# weekends in Sofia: 48 - weekends_out_count
saturday_games = 3 / 4 * (48 - weekends_out_count)
vacations_games = 2 / 3 * vacations_days_count

total_games = vacations_games + saturday_games + weekends_out_count

if year_type == "leap":
    total_games += 0.15 * total_games

print(f"{math.floor(total_games)}")