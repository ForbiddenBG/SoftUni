lenght = int(input())
width = int(input())
highth = int(input())

percentige = float(input())

acuarium_size = lenght * width * highth

usage = percentige / 100

water = acuarium_size - (usage * acuarium_size)
liters = water / 1000

print(liters)
