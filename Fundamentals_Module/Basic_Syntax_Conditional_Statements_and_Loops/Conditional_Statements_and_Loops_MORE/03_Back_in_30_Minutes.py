hours = int(input())
minutes = int(input())

time_after_half = minutes + 30

if time_after_half > 59:
    hours += 1
    rest = time_after_half - 60
else:
    rest = time_after_half

if hours == 24:
    hours = 0
elif hours > 24:
    hours -= 24


print(f"{hours}:{rest:02d}")
