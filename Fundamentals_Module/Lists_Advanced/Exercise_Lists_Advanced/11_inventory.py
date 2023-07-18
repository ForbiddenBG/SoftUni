inventory = input().split(", ")

command = input()
while not command == "Craft!":
    work, item = command.split(" - ")
    if work == "Collect":
        if item not in inventory:
            inventory.append(item)
        else:
            pass
    if work == "Drop":
        if item in inventory:
            inventory.remove(item)
        else:
            pass
    if work == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in inventory:
            old_index = inventory.index(old_item)
            inventory.insert(old_index + 1, new_item)
        else:
            pass
    if work == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
        else:
            pass
    command = input()

print(", ".join(inventory))


# def check_item_exist(items_list, item):
#     if item in items_list:
#         return True
#     return False
#
# def add_item(items_list, item):
#     if not check_item_exist(items_list, item):
#         items_list.append(item)
#     return items_list
#
# def remove_item(items_list, item):
#     if check_item_exist(items_list, item):
#         items_list.remove(item)
#     return items_list
#
# def combine_item(items_list, items_data):
#     old_item, new_item = items_data.split(":")
#     if check_item_exist(items_list, old_item):
#         index_old_item = items_list.index(old_item)
#         items_list.insert(index_old_item + 1, new_item)
#     return items_list
#
# def renew_item(items_list, item):
#     if check_item_exist(items_list, item):
#         items_list.remove(item)
#         items_list.append(item)
#     return items_list
#
# items = input().split(", ")
# command_data = input()
#
#
# while not command_data == "Craft!":
#     command, item = command_data.split(" - ")
#     if command == "Collect":
#         items = add_item(items, item)
#     else:
#         pass
#     if command == "Drop":
#         items = remove_item(items, item)
#     else:
#         pass
#     if command == "Combine Item":
#         items = combine_item(items, item)
#     else:
#         pass
#     if command == "Renew":
#         items = renew_item(items, item)
#     else:
#         pass
#     command_data = input()
#
# print(*items, sep=", ")
