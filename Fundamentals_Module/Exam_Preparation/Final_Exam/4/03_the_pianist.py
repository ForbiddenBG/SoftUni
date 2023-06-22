n = int(input())
pieces = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

data = input()

while not data == "Stop":
    split_data = data.split("|")
    if split_data[0] == "Add":
        piece, composer, key = split_data[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif split_data[0] == "Remove":
        piece = split_data[1]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
    elif split_data[0] == "ChangeKey":
        piece, new_key = split_data[1:]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    data = input()

sorted_pieces = sorted(pieces.items(), key=lambda kvpt: (kvpt[0], kvpt[1]["composer"]))

for piece, data in sorted_pieces:
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")
