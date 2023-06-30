text = input()

command = input()
while not command == "For Azeroth":
    main_data = command.split()
    if main_data[0] == "GladiatorStance":
        text = text.upper()
        print(text)
    elif main_data[0] == "DefensiveStance":
        text = text.lower()
        print(text)
    elif main_data[0] == "Dispel":
        index, letter = main_data[1:]
        index = int(index)
        if 0 <= index < len(text):
            text = text[0:index] + letter + text[index+1:]
            print("Success!")
        else:
            print("Dispel too weak.")
    elif main_data[0] == "Target":
        if main_data[1] == "Change":
            substring, second_substring = main_data[2:]
            text = text.replace(substring, second_substring)
        elif main_data[1] == "Remove":
            substring = main_data[2]
            text = text.replace(substring, "")
        print(text)
    elif main_data[0] == "Target Remove":
        substring = main_data[1]
        text = text.replace(substring, "")
        print(text)
    else:
        print("Command doesn't exist!")
    command = input()
