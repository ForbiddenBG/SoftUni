string = input()

command = input()
while not command == "End":
    main_data = command.split()
    if main_data[0] == "Translate":
        char, replacement = main_data[1:]
        string = string.replace(char, replacement)
        print(string)
    elif main_data[0] == "Includes":
        substring = main_data[1]
        if substring in string:
            print(True)
        else:
            print(False)
    elif main_data[0] == "Start":
        substring = main_data[1]
        if string.startswith(substring):
            print(True)
        else:
            print(False)
    elif main_data[0] == "Lowercase":
        string = string.lower()
        print(string)
    elif main_data[0] == "FindIndex":
        char = main_data[1]
        index = string.rfind(char)
        print(index)
    elif main_data[0] == "Remove":
        start_index, count = main_data[1:]
        start_index = int(start_index)
        count = int(count)
        string = string[0:start_index] + string[start_index+count:]
        print(string)
    command = input()
