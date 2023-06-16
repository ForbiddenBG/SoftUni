info = input()

phonebook = {}

while "-" in info:
    name, phone = info.split("-")
    phonebook[name] = phone
    info = input()

for _ in range(int(info)):
    name = input()
    if name not in phonebook:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")
