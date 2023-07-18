# def check_if_index_is_valid(index, len_list):
#     if index in range(len_list):
#         return True
#     return False
#
#
# targets = [int(el) for el in input().split()]
#
# command_data = input()
#
# while not command_data == "End":
#     command, index, val = command_data.split()
#     index = int(index)
#     val = int(val)
#     if command == "Shoot":
#         if check_if_index_is_valid(index, len(targets)):
#             targets[index] -= val
#             if targets[index] <= 0:
#                 targets.pop(index)
#     elif command == "Add":
#         if check_if_index_is_valid(index, len(targets)):
#             targets.insert(index, val)
#         else:
#             print("Invalid placement!")
#     elif command == "Strike":
#         left_most_index = index - val
#         right_most_index = index + val
#         if check_if_index_is_valid(index, len(targets)) and check_if_index_is_valid(left_most_index, len(targets)) and check_if_index_is_valid(right_most_index, len(targets)):
#             left_unstriked_part = targets[:index]
#             right_unstriked_part = targets[right_most_index+1:]
#             targets = left_unstriked_part + right_unstriked_part
#         else:
#             print("Strike missed!")
#
#     command_data = input()
#
# print('|'.join([str(el) for el in targets]))

def shoot_target(targets, current_index, current_value):
    targets[current_index] -= current_value
    if targets[current_index] <= 0:
        targets.pop(current_index)
    return targets


def add_target(targets, current_index, current_value):
    targets.insert(current_index, current_value)
    return targets


def strike_target(targets, current_index, current_value):
    targets = targets[0: current_index - current_value] + targets[current_index + current_value + 1::]
    return targets


sequence_of_targets = [int(number) for number in input().split()]
command = input().split()
while command[0] != "End":
    action = command[0]
    index = int(command[1])
    value = int(command[2])
    if action == "Shoot":
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets = shoot_target(sequence_of_targets, index, value)
    elif action == "Add":
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets = add_target(sequence_of_targets, index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if 0 <= index - value < len(sequence_of_targets) and 0 <= index + value < len(sequence_of_targets):
            sequence_of_targets = strike_target(sequence_of_targets, index, value)
        else:
            print("Strike missed!")
    command = input().split()
print('|'.join(str(target) for target in sequence_of_targets))
