initial_list = input().split("!")

command = input()
while not command == "Go Shopping!":
    main_data = command.split()
    data = main_data[0]
    if data == "Urgent":
        old_item = main_data[1]
        if old_item not in initial_list:
            initial_list.insert(0, old_item)
        else:
            pass
    if data == "Unnecessary":
        old_item = main_data[1]
        if old_item in initial_list:
            initial_list.remove(old_item)
        else:
            pass
    if data == "Correct":
        old_item = main_data[1]
        new_item = main_data[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list.remove(old_item)
            initial_list.insert(index, new_item)
        else:
            pass
    if data == "Rearrange":
        old_item = main_data[1]
        if old_item in initial_list:
            initial_list.remove(old_item)
            initial_list.append(old_item)
        else:
            pass
    command = input()

print(", ".join(initial_list))
