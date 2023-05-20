from math import floor

n = int(input())

points = 0
red_balls_num = 0
orange_balls_num = 0
yellow_balls_num = 0
white_balls_num = 0
other_colors_num = 0
divide_num = 0

for n in range(0, n):
    colors = input()
    if colors == "red":
        points += 5
        red_balls_num += 1
    elif colors == "orange":
        points += 10
        orange_balls_num += 1
    elif colors == "yellow":
        points += 15
        yellow_balls_num += 1
    elif colors == "white":
        points += 20
        white_balls_num += 1
    elif colors == "black":
        points /= 2
        divide_num += 1
    else:
        other_colors_num += 1
        continue
print()


print(f"Total points: {floor(points)}")
print(f"Points from red balls: {red_balls_num}")
print(f"Points from orange balls: {orange_balls_num}")
print(f"Points from yellow balls: {yellow_balls_num}")
print(f"Points from white balls: {white_balls_num}")
print(f"Other colors picked: {other_colors_num}")
print(f"Divides from black balls: {divide_num}")
