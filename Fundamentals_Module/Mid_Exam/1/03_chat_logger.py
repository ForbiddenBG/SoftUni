my_list = []
command = input()
while not command == "end":
    main_data = command.split()
    data = main_data[0]
    if data == "Chat":
        message = main_data[1]
        my_list.append(message)
    if data == "Delete":
        message = main_data[1]
        if message in my_list:
            my_list.remove(message)
        else:
            pass
    if data == "Edit":
        message = main_data[1]
        edited = main_data[2]
        if message in my_list:
            index = my_list.index(message)
            my_list.pop(index)
            my_list.insert(index, edited)
        else:
            pass
    if data == "Pin":
        message = main_data[1]
        if message in my_list:
            my_list.remove(message)
            my_list.append(message)
        else:
            pass
    if data == "Spam":
        for message in main_data[1:]:
            my_list.append(message)

    command = input()

print("\n".join(my_list))
