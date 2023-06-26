emails = {}
total_count_of_users = 0

command = input()
while not command == "Statistics":
    main_data = command.split("->")
    if main_data[0] == "Add":
        username = main_data[1]
        if username in emails:
            print(f"{username} is already registered")
        else:
            emails[username] = []
            total_count_of_users += 1
    elif main_data[0] == "Send":
        username, email = main_data[1:]
        emails[username].append(email)
    elif main_data[0] == "Delete":
        username = main_data[1]
        if username in emails:
            del emails[username]
            total_count_of_users -= 1
        else:
            print(f"{username} not found!")
    command = input()

sorted_users = sorted(emails.items(), key=lambda kvp: kvp[0][0])

print(f"Users count: {total_count_of_users}")
for key, value in sorted_users:
    print(f"{key}")
    for el in value:
        print(f" - {''.join(el)}")
