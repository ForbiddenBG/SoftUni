followers = {}
count_followers = 0

command = input()
while not command == "Log out":
    main_data = command.split(": ")
    if main_data[0] == "New follower":
        username = main_data[1]
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}
            count_followers += 1
    elif main_data[0] == "Like":
        username, count = main_data[1:]
        count = int(count)
        if username not in followers:
            followers[username] = {'likes': count, 'comments': 0}
            count_followers += 1
        else:
            followers[username]['likes'] += count
    elif main_data[0] == "Comment":
        username = main_data[1]
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 1}
            count_followers += 1
        else:
            followers[username]['comments'] += 1
    elif main_data[0] == "Blocked":
        username = main_data[1]
        if username in followers:
            del followers[username]
            count_followers -= 1
        else:
            print(f"{username} doesn't exist.")
    command = input()

sorted_followers = sorted(followers.items(), key=lambda kvp: (-kvp[1]['likes'], kvp[0]))

print(f"{count_followers} followers")
for key, value in sorted_followers:
    print(f"{key}: {value['likes'] + value['comments']}")
