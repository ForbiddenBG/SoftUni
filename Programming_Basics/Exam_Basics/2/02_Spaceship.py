from math import floor

ship_width = float(input())
ship_length = float(input())
ship_highth = float(input())
averrage_ast_highth = float(input())

ship_cap = ship_highth * ship_length * ship_width
room_size = (averrage_ast_highth + 0.40) * 2 * 2
room_for = floor(ship_cap / room_size)

if 3 <= room_for <= 10:
    print(f"The spacecraft holds {room_for} astronauts.")
elif room_for < 3:
    print(f"The spacecraft is too small.")
else:
    print(f"The spacecraft is too big.")
