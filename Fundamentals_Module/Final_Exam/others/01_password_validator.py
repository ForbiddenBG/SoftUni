import re

password = input()
pattern = r"^\w+$"

command = input()
while not command == "Complete":
    main_data = command.split()
    if main_data[0] == "Make":
        index = int(main_data[2])
        if index in range(len(password)):
            if main_data[1] == "Upper":
                password = password[0:index] + password[index].upper() + password[index+1:]
            elif main_data[1] == "Lower":
                password = password[0:index] + password[index].lower() + password[index+1:]
            print(password)
    elif main_data[0] == "Insert":
        index, char = main_data[1:]
        index = int(index)
        if index in range(len(password)):
            password = password[0:index] + char + password[index:]
            print(password)
        else:
            pass
    elif main_data[0] == "Replace":
        char, value = main_data[1:]
        value = int(value)
        if char in password:
            value_of_char = ord(char)
            sum_of_values = value + value_of_char
            new_char = chr(sum_of_values)
            password = password.replace(char, new_char)
            print(password)
        else:
            pass
    elif main_data[0] == "Validation":
        is_upper = False
        is_lower = False
        is_digit = False

        for el in password:
            if el.isdigit():
                is_digit = True
            if el.isupper():
                is_upper = True
            if el.islower():
                is_lower = True

        match = re.match(pattern, password)

        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        if not match:
            print("Password must consist only of letters, digits and _!")
        if not is_upper:
            print("Password must consist at least one uppercase letter!")
        if not is_lower:
            print("Password must consist at least one lowercase letter!")
        if not is_digit:
            print("Password must consist at least one digit!")

    command = input()
