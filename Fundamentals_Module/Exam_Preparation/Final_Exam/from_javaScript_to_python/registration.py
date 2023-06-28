import re

number = int(input())
count = 0

for _ in range(number):
    text = input()
    pattern = r"(U\$)(?P<username>[A-Z][a-z]{2,})\1(P\@\$)(?P<password>[a-zA-Z]{5,}[0-9]+)(\3)"
    valid_registration = [el.groupdict() for el in re.finditer(pattern, text)]
    if valid_registration:
        for i in valid_registration:
            print("Registration was successful")
            print(f"Username: {i['username']}, Password: {i['password']}")
            count += 1
    else:
        print(f"Invalid username or password")

print(f"Successful registrations: {count}")
