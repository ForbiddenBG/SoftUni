text = input()
new_pass = ""

command = input()
while not command == "Done":
    main_data = command.split()
    if main_data[0] == "TakeOdd":
        for el in range(len(text)):
            if el % 2 == 1:
                new_pass += text[el]
        text = new_pass
        print(text)
    elif main_data[0] == "Cut":
        index, length = main_data[1:]
        index = int(index)
        length = int(length)
        text = text[:index] + text[index + length:]
        print(text)
    elif main_data[0] == "Substitute":
        substring, substitute = main_data[1:]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {text}")
