numbers = input().split()

left_car_time = 0.0
right_car_time = 0.0

for time in range(len(numbers)):
    left_time = float(numbers[time])
    left_car_time += left_time
    if left_time == 0 and not time == 5:
        left_car_time *= 0.8
    if time == 5:
        break

for second_t in range(len(numbers), -1, -1):
    right_time = float(numbers[second_t])
    left_car_time += right_time
    if right_time == 0 and not second_t == 5:
        right_car_time *= 0.8
    if second_t == 5:
        break

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")
