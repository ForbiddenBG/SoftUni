from math import ceil
days_count = int(input())
first_day_km = float(input())

run_km = first_day_km
total_km = first_day_km

for day in range(1, days_count + 1):
    percent_increce = int(input()) / 100
    run_km += run_km * percent_increce
    total_km += run_km

diff = ceil(abs(1000 - total_km))
if total_km < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")
else:
    print(f"You've done a great job running {diff} more kilometers!")


