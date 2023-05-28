command = input()

coffees = 0

while not command == "END":
    if command == command.upper():
        if command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
            coffees += 2
        else:
            pass
    if command == command.lower():
        if command == "coding" or command == "dog" or command == "cat" or command == "movie":
            coffees += 1
        else:
            pass

    command = input()

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
