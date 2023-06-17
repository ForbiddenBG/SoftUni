count = int(input())
parking = {}

for _ in range(count):
    data = input()
    split_data = data.split()
    command = split_data[0]

    if command == "register":
        username = split_data[1]
        license = split_data[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license}")
        else:
            parking[username] = license
            print(f"{username} registered {license} successfully")
    elif command == "unregister":
        username = split_data[1]
        if username not in parking:
            print(f"ERROR: {username} not not found")
        else:
            del parking[username]
            # parking.pop(username)
            print(f"{username} unregistered successfully")

for username, license in parking.items():
    print(f"{username} => {license}")
