text = input()

command = input()
while not command == "Finish":
    main_data = command.split()
    if main_data[0] == "Replace":
        current_char, new_char = main_data[1:]
        text = text.replace(current_char, new_char)
        print(text)
    elif main_data[0] == "Cut":
        start_index, end_index = main_data[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if 0 <= start_index < end_index < len(text):
            text = text[0:start_index] + text[end_index:]
            print(text)
        else:
            print("Invalid indexes!")
    elif main_data[0] == "Make":
        if main_data[1] == "Upper":
            text = text.upper()
        else:
            text = text.lower()
        print(text)
    elif main_data[0] == "Check":
        if main_data[1] in text:
            print(f"Message contains {main_data[1]}")
        else:
            print(f"Message doesn't contain {main_data[1]}")
    elif main_data[0] == "Sum":
        start_index, end_index = main_data[1:]
        start_index, end_index = int(start_index), int(end_index)
        substring = text[start_index:end_index+1]
        sum_of_the_values = 0
        if 0 <= start_index < end_index < len(text):
            for el in substring:
                sum_of_the_values += ord(el)
            print(sum_of_the_values)
        else:
            print(f"Invalid indexes!")

    command = input()
