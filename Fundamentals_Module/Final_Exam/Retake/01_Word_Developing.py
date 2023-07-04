string = ""
my_list = []

command = input()
while not command == "End":
    main_data = command.split()
    if main_data[0] == "Add":
        substring = main_data[1]
        string = string + substring
    elif main_data[0] == "Upgrade":
        char = main_data[1]
        string = string.replace(char, chr(ord(char) + 1))
    elif main_data[0] == "Print":
        print(string)
    elif main_data[0] == "Index":
        char = main_data[1]
        if char in string:
            my_list.extend([str(i) for i, x in enumerate(string) if x == char])
            print(f"{' '.join(my_list)}")
        else:
            print(None)
    elif main_data[0] == "Remove":
        substring = main_data[1]
        string = string.replace(substring, "")
    command = input()
