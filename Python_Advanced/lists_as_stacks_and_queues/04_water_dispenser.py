from collections import deque

start_quantity = int(input())
line = deque()

command = input()
while not command == "Start":
    line.append(command)
    command = input()

liters = input()
while not liters == "End":
    main_data = liters.split()
    if main_data[0] == "refill":
        water = int(main_data[1])
        start_quantity += water
    else:
        if start_quantity >= int(main_data[0]):
            start_quantity -= int(main_data[0])
            print(f"{line.popleft()} got water")
        else:
            print(f"{line.popleft()} must wait")
    liters = input()

print(f"{start_quantity} liters left")

# from collections import deque
#
# start_quantity = int(input())
# line = deque()
#
# command = input()
# while not command == "Start":
#     line.append(command)
#     command = input()
#
# liters = input()
# while not liters == "End":
#     if liters.isdigit():
#         liters = int(liters)
#         name = line.popleft()
#         if start_quantity >= liters:
#             start_quantity -= liters
#             print(f"{name} got water")
#         else:
#             print(f"{name} must wait")
#     else:
#         _, water = liters.split()
#         water = int(water)
#         start_quantity += water
#     liters = input()
#
# print(f"{start_quantity} liters left")

# from collections import deque
# quantity = int(input())
#
# names = deque()
#
# text = input()
# while not text == "Start":
#     names.append(text)
#     text = input()
#
# commands = input()
# while not commands == "End":
#     if commands.isdigit():
#         if int(commands) <= quantity:
#             quantity -= int(commands)
#             print(f"{names.popleft()} got water")
#         else:
#             print(f"{names.popleft()} must wait")
#     elif commands.startswith("refill"):
#         _, liters = commands.split()
#         quantity += int(liters)
#     commands = input()
#
# print(f"{quantity} liters left")
