username = input()

command = input()
while not command == "Sign up":
    main_data = command.split()
    if main_data[0] == "Case":
        case = main_data[1]
        if case == "lower":
            username = username.lower()
        else:
            username = username.upper()
        print(username)
    elif main_data[0] == "Reverse":
        start_index, end_index = main_data[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if start_index in range(len(username)) and end_index in range(len(username)):
            reverse = username[start_index:start_index+end_index]
            print(reverse[::-1])
    elif main_data[0] == "Cut":
        substring = main_data[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif main_data[0] == "Replace":
        char = main_data[1]
        username = username.replace(char, "*")
        print(username)
    elif main_data[0] == "Check":
        char = main_data[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    command = input()
