messages = {}
users_count = 0

capacity = int(input())

command = input()
while not command == "Statistics":
    main_data = command.split("=")
    if main_data[0] == "Add":
        username, sent, received = main_data[1:]
        sent = int(sent)
        received = int(received)
        if username not in messages:
            messages[username] = {'sent': sent, 'received': received}
            users_count += 1
    elif main_data[0] == "Message":
        sender, receiver = main_data[1:]
        if sender in messages and receiver in messages:
            messages[sender]['sent'] += 1
            messages[receiver]['received'] += 1
            if messages[sender]['sent'] + messages[sender]['received'] >= capacity:
                del messages[sender]
                users_count -= 1
                print(f"{sender} reached the capacity!")
            if messages[receiver]['sent'] + messages[receiver]['received'] >= capacity:
                del messages[receiver]
                users_count -= 1
                print(f"{receiver} reached the capacity!")
    elif main_data[0] == "Empty":
        username = main_data[1]
        if username in messages:
            del messages[username]
            users_count -= 1
        elif username == "All":
            messages = {}
            users_count = 0
    command = input()


sorted_users = sorted(messages.items(), key=lambda kvp: (-kvp[1]['received'], kvp[0]))

print(f"Users count: {users_count}")
for key, value in sorted_users:
    print(f"{key} - {value['sent'] + value['received']}")
