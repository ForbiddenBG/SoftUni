text = input()

command = input()
while not command == "Travel":
    main_data = command.split(":")

    if main_data[0] == "Add Stop":
        index, string = main_data[1:]
        index = int(index)
        if index in range(len(text)):
            text = text[0:index] + string + text[index:]
        print(text)

    elif main_data[0] == "Remove Stop":
        start_index, end_index = main_data[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if start_index in range(len(text)) and end_index in range(len(text)):
            text = text[0:start_index] + text[end_index+1:]
        print(text)

    elif main_data[0] == "Switch":
        old_string, new_string = main_data[1:]
        if old_string in text:
            text = text.replace(old_string, new_string)
        print(text)

    command = input()

print(f"Ready for world tour! Planned stops: {text}")
