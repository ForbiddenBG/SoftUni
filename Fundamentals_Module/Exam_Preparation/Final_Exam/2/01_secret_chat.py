secret_message = input()

data = input()

while not data == "Reveal":
    split_data = data.split(":|:")
    if split_data[0] == "InsertSpace":
        index = int(split_data[1])
        secret_message = secret_message[0:index] + " " + secret_message[index:]
        print(secret_message)
    elif split_data[0] == "Reverse":
        substring = split_data[1]
        if substring not in secret_message:
            print("error")
        else:
            secret_message = secret_message.replace(substring, "", 1)
            reversed_substring = substring[::-1]
            secret_message += reversed_substring
            print(secret_message)
    elif split_data[0] == "ChangeAll":
        substring, replace_str = split_data[1:]
        secret_message = secret_message.replace(substring, replace_str)
        print(secret_message)
    data = input()

print(f"You have a new text message: {secret_message}")
