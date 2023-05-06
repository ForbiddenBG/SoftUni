name = input()

is_mammal = name == "dog"
is_reptile = name == "crocodile" or \
    name == "tortoise" or \
    name == "snake"

if is_mammal:
    print("mammal")
elif is_reptile:
    print("reptile")
else:
    print("unknown")