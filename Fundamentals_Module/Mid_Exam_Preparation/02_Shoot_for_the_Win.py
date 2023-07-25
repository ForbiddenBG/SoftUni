targets = [int(el) for el in input().split()]

shoot_targets = 0

command = input()
while not command == "End":
    index = int(command)
    if index in range(len(targets)) and targets[index] > - 1:
        shoot_targets += 1
        removed = targets[index]
        targets.pop(index)
        targets.insert(index, -1)
        for target in range(len(targets)):
            if targets[target] == -1:
                continue
            if targets[target] > removed:
                new_value = targets[target] - removed
                targets.pop(target)
                targets.insert(target, new_value)
            else:
                new_value = targets[target] + removed
                targets.pop(target)
                targets.insert(target, new_value)

    command = input()

print(f"Shot targets: {shoot_targets} -> {' '.join([str(el) for el in targets])}")

# targets = [int(el) for el in input().split()]
#
# index = input()
# counter_shot_targets = 0
#
# while not index == "End":
#     index = int(index)
#
#     if index in range(len(targets)):
#         index = input()
#         continue
#
#     current_value = targets[index]
#
#     if current_value == -1:
#         index = input()
#         continue
#
#     targets[index] = -1
#     counter_shot_targets += 1
#
#     for current_index in range(len(targets)):
#         if targets[current_index] == -1:
#             continue
#         if targets[current_index] > current_value:
#             targets[current_index] -= current_value
#         else:
#             targets[current_index] += current_value
#
#     index = input()
#
# print(f"Shot targets: {counter_shot_targets} -> {' '.join([str(el) for el in targets])}")
