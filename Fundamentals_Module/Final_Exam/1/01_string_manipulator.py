text = input()

command = input()
while not command == "End":
    main_data = command.split()
    if main_data[0] == "Translate":
        char, replacement = main_data[1:]
        text = text.replace(char, replacement)
        print(text)
    elif main_data[0] == "Includes":
        substring = main_data[1]
        if substring in text:
            print(True)
        else:
            print(False)
    elif main_data[0] == "Start":
        substring = main_data[1]
        if text.startswith(substring):
            print(True)
        else:
            print(False)
    elif main_data[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif main_data[0] == "FindIndex":
        char = main_data[1]
        index = text.rfind(char)
        print(index)
    elif main_data[0] == "Remove":
        start_index, count = main_data[1:]
        start_index = int(start_index)
        count = int(count)
        text = text[0:start_index] + text[start_index+count:]
        print(text)

    command = input()
