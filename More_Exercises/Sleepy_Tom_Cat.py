holidays_count = int(input())

norm_per_year = 30000
one_year = 365
when_he_works = 63
when_he_rests = 127

total_work_days = one_year - holidays_count
total_time_for_play = total_work_days * when_he_works + holidays_count * when_he_rests
difference = norm_per_year - total_time_for_play
in_hours = difference // 60
in_minutes = difference % 60

if total_time_for_play >= norm_per_year:
    print(f"Tom will run away")
    if in_minutes > 59:
        in_minutes -= 60
        in_hours += 1

    if in_hours > 23:
        in_hours -= 24

    if in_minutes < 10:
        print(f"{in_hours} hours and {in_minutes} minutes more for play")
    else:
        print(f"{in_hours} hours and {in_minutes} minutes more for play")
else:
    print(f"Tom sleeps well")
    if in_minutes > 59:
        in_minutes -= 60
        in_hours += 1

    if in_hours > 23:
        in_hours -= 24

    if in_minutes < 10:
        print(f"{in_hours} hours and {in_minutes} minutes less for play")
    else:
        print(f"{in_hours} hours and {in_minutes} minutes less for play")