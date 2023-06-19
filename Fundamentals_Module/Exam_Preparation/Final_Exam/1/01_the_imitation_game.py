encoded_massage = input()

command = input()
while not command == "Decode":
    main_data = command.split("|")
    if main_data[0] == "Move":
        number = int(main_data[1])
        encoded_massage = encoded_massage[number:] + encoded_massage[:number]

    elif main_data[0] == "Insert":
        index = int(main_data[1])
        value = main_data[2]
        encoded_massage = encoded_massage[:index] + value + encoded_massage[index:]

    elif main_data[0] == "ChangeAll":
        substring = main_data[1]
        replacement = main_data[2]
        encoded_massage = encoded_massage.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encoded_massage}")
