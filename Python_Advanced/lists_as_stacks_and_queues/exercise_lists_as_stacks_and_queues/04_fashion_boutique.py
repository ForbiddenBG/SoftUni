clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_counter = 1
current_rack = rack_capacity

while clothes:
    current_piece = clothes[-1]
    if current_piece <= current_rack:
        current_rack -= current_piece
        clothes.pop()
    else:
        rack_counter += 1
        current_rack = rack_capacity

print(rack_counter)

# clothes = [int(x) for x in input().split()]
# rack_capacity = int(input())
#
# max_rack_capacity = rack_capacity
# used_racks = 1
#
# while clothes:
#     if max_rack_capacity < clothes[-1]:
#         used_racks += 1
#         max_rack_capacity = rack_capacity
#     max_rack_capacity -= clothes[-1]
#     clothes.pop()
#
# print(used_racks)
