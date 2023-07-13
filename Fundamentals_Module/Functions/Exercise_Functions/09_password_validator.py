def password_validator(pword):
    is_valid = True
    counter = 0

    if len(pword) < 6 or len(pword) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    for char in pword:
        if char.isdigit():
            counter += 1
        if not char.isalpha() and not char.isdigit():
            is_valid = False
            print("Password must consist only of letters and digits")
            break

    if counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid and counter >= 2:
        print("Password is valid")


password = input()
password_validator(password)
