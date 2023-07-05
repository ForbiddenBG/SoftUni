string = input()

command = input()
while not command == "Done":
    main_data = command.split()
    if main_data[0] == "Change":
        char, replacement = main_data[1:]
        string = string.replace(char, replacement)
        print(string)
    elif main_data[0] == "Includes":
        substring = main_data[1]
        if substring in string:
            print(True)
        else:
            print(False)
    elif main_data[0] == "End":
        substring = main_data[1]
        if string.endswith(substring):
            print(True)
        else:
            print(False)
    elif main_data[0] == "Uppercase":
        string = string.upper()
        print(string)
    elif main_data[0] == "FindIndex":
        char = main_data[1]
        index = string.index(char)
        print(index)
    elif main_data[0] == "Cut":
        start_index, count = main_data[1:]
        start_index = int(start_index)
        count = int(count)
        string = string[start_index:start_index+count]
        print(string)

    command = input()
