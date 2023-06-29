text = input()

command = input()
while not command == "Done":
    main_data = command.split()
    if main_data[0] == "Change":
        char, replacement = main_data[1:]
        text = text.replace(char, replacement)
        print(text)
    elif main_data[0] == "Includes":
        string = main_data[1]
        if string in text:
            print(True)
        else:
            print(False)
    elif main_data[0] == "End":
        string = main_data[1]
        if text.endswith(string):
            print(True)
        else:
            print(False)
    elif main_data[0] == "Uppercase":
        text = text.upper()
        print(text)
    elif main_data[0] == "FindIndex":
        char = main_data[1]
        index = text.index(char)
        print(index)
    elif main_data[0] == "Cut":
        start_string, length = main_data[1:]
        start_string = int(start_string)
        length = int(length)
        text = text[start_string:start_string+length]
        print(text)
    command = input()
