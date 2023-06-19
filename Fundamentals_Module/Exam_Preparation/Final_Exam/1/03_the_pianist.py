number_of_pieces = int(input())

collection = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    collection[piece] = {'composer': composer, 'key': key}

command = input()
while not command == "Stop":
    main_data = command.split("|")
    if main_data[0] == "Add":
        piece, composer, key = main_data[1:]
        if piece not in collection:
            collection[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif main_data[0] == "Remove":
        piece = main_data[1]
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif main_data[0] == "ChangeKey":
        piece, new_key = main_data[1:]
        if piece in collection:
            collection[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

sorted_pieces = sorted(collection.items(), key=lambda kvpt: (kvpt[0], kvpt[1]['composer']))

for k, v in sorted_pieces:
    print(f'{k} -> Composer: {v["composer"]}, Key: {v["key"]}')
