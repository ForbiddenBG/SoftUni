length = float(input())
width = float(input())

desk_length = 120
desk_width = 70

hall_length = length * 100
hall_width = (width * 100) - 100
desks_per_l = hall_length // desk_length
desks_per_w = hall_width // desk_width
desks = desks_per_l * desks_per_w - 3

print(desks)
