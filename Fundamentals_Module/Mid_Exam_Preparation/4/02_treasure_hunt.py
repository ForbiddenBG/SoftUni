inventory = input().split("|")

command = input()
while not command == "Yohoho!":
    data = command.split()
    if data[0] == "Loot":
        for item in data[1:]:
            if item not in inventory:
                inventory.insert(0, item)
    elif data[0] == "Drop":
        index = int(data[1])
        if index < 0 or index >= len(inventory):
            command = input()
            continue
        removed = inventory.pop(index)
        inventory.append(removed)
    elif data[0] == "Steal":
        count = int(data[1])
        removed = inventory[-count:]
        print(", ".join(removed))
        inventory = inventory[:-count]
    command = input()

length = len(inventory)

if length == 0:
    print("Failed treasure hunt.")
else:
    sume = 0
    for item in inventory:
        sum += len(item)
    avg_gain = sume / length
    print(f"Average treasure gain: {avg_gain:.2f} pirate credits.")

# command_input = input()
#
# while command_input != "Yohoho!":
#     command_arg = command_input.split()
#     command = command_arg[0]
#
#     if command == "Loot":
#         items = command_arg[1:]
#         for item in items:
#             if item not in chest:
#                 chest.insert(0, item)
#
#     elif command == "Drop":
#         index = int(command_arg[1])
#         if index < 0 or index >= len(chest):
#             command_input = input()
#             continue
#         removed_item = chest.pop(index)
#         chest.append(removed_item)
#
#     elif command == "Steal":
#         count = int(command_arg[1])
#         removed_items = chest[-count:]
#         print(", ".join(removed_items))
#         chest = chest[:-count]
#
#     command_input = input()
#
# length_of_chest = len(chest)
#
# if length_of_chest == 0:
#     print("Failed treasure hunt.")
# else:
#     sum = 0
#     for item in chest:
#         sum += len(item)
#     average = sum / length_of_chest
#     print(f"Average treasure gain: {average:.2f} pirate credits.")
