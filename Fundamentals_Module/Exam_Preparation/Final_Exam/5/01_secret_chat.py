concealed_message = input()

command = input()
while not command == "Reveal":
    main_data = command.split(":|:")
    if main_data[0] == "InsertSpace":
        index = int(main_data[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(f"{concealed_message}")
    elif main_data[0] == "Reverse":
        substring = main_data[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
            print(f"{concealed_message}")
        else:
            print("error")
    elif main_data[0] == "ChangeAll":
        substring, replacement = main_data[1:]
        concealed_message = concealed_message.replace(substring, replacement)
        print(f"{concealed_message}")
    command = input()

print(f"You have a new text message: {concealed_message}")
