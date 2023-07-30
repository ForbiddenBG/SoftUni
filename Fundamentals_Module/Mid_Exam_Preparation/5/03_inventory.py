inventory = input().split(", ")


command = input()
while not command == "Craft!":
    command, item = command.split(" - ")
    if command == "Collect":
        if item not in inventory:
            inventory.append(item)
        else:
            pass
    elif command == "Drop":
        if item in inventory:
            inventory.remove(item)
        else:
            pass
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in inventory:
            index = inventory.index(old_item)
            inventory.insert(index + 1, new_item)
        else:
            pass
    elif command == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
        else:
            pass
    command = input()

print(", ".join(inventory))
