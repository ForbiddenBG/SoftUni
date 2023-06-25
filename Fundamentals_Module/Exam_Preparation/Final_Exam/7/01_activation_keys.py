text = input()

command = input()
while not command == "Generate":
    main_data = command.split(">>>")
    if main_data[0] == "Contains":
        substring = main_data[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print(f"Substring not found!")
    elif main_data[0] == "Flip":
        upper_lower, start_index, end_index = main_data[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if upper_lower == "Upper":
            text = text[0:start_index] + text[start_index:end_index].upper() + text[end_index:]

        else:
            text = text[0:start_index] + text[start_index:end_index].lower() + text[end_index:]
        print(text)
    elif main_data[0] == "Slice":
        start_index, end_index = main_data[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        text = text[0:start_index] + text[end_index:]
        print(text)
    command = input()

print(f"Your activation key is: {text}")
