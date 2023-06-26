text = input()

command = input()
while not command == "Complete":
    main_data = command.split()
    if main_data[0] == "Make":
        if main_data[1] == "Upper":
            text = text.upper()
            print(text)
        else:
            text = text.lower()
            print(text)
    elif main_data[0] == "GetDomain":
        count = int(main_data[1])
        print(text[-count:])
    elif main_data[0] == "GetUsername":
        substring = ""
        for el in text:
            if "@" in text:
                if not el == "@":
                    substring += el
                else:
                    print(substring)
            else:
                print(f"The email {text} doesn't contain the @ symbol.")
                break
        substring = ""
    elif main_data[0] == "Replace":
        char = main_data[1]
        text = text.replace(char, "-")
        print(text)
    elif main_data[0] == "Encrypt":
        encrypted = []
        for el in text:
            encrypted.append(str(ord(el)))
        print(*encrypted, end=" ")

    command = input()
