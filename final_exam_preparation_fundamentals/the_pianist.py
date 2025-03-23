number_of_pieces = int(input())
pieces_collection = {}

for i in range(number_of_pieces):
    piece, composer, key = piece_composer_key = input().split("|")
    pieces_collection[piece] = (composer, key)

while True:
    command = input()
    if command == "Stop":
        break
    command_type = command.split("|")
    action = command_type[0]

    if action == "Add":
        piece = command_type[1]
        composer = command_type[2]
        key = command_type[3]
        if piece in pieces_collection:
            print(f"{piece} is already in the collection!")
        else:
            pieces_collection[piece] = (composer, key)
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        piece = command_type[1]
        if piece in pieces_collection:
            del pieces_collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece = command_type[1]
        new_key = command_type[2]
        if piece in pieces_collection:
            composer, current_key = pieces_collection[piece]
            pieces_collection[piece] = (composer, new_key)
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, (composer, key) in pieces_collection.items():
    print(f"{piece} -> Composer: {composer}, Key: {key}")
