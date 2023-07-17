n_rooms = int(input())
are_chairs_enough = True
free_chairs = 0

for room_num in range(1, n_rooms + 1):
    chairs, n_people = input().split()
    n_people = int(n_people)
    difference = abs(len(chairs) - n_people)
    if len(chairs) < n_people:
        print(f"{difference} more chairs needed in room {room_num}")
        are_chairs_enough = False
    else:
        free_chairs += difference


if are_chairs_enough:
    print(f"Game On, {free_chairs} free chairs left")

# rooms_count = int(input())
#
# rest = 0
# is_positive = True
#
# for room in range(1, rooms_count + 1):
#     data = input().split()
#     chairs = data[0].count("X")
#     visitors = int(data[1])
#     if chairs < visitors:
#         print(f"{abs(chairs - visitors)} more chairs needed in room {room}")
#         is_positive = False
#     else:
#         rest += (chairs - visitors)
#
# if is_positive:
#     print(f"Game On, {rest} free chairs left")
