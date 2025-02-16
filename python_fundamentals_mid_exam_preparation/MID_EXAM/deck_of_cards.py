card_deck = input().split(", ")
n = int(input())

for i in range(n):
    command_type = input().split(", ")
    action = command_type[0]

    if action == "Add":
        card_name = command_type[1]
        if card_name in card_deck:
            print("Card is already in the deck")
        else:
            card_deck.append(card_name)
            print("Card successfully added")

    elif action == "Remove":
        card_name = command_type[1]
        if card_name not in card_deck:
            print("Card not found")
        else:
            card_deck.remove(card_name)
            print("Card successfully removed")

    elif action == "Remove At":
        index = int(command_type[1])
        if index not in range(0, len(card_deck)):
            print("Index out of range")
        else:
            card_deck.pop(index)
            print("Card successfully removed")

    elif action == "Insert":
        index = int(command_type[1])
        card_name = command_type[2]
        if index not in range(0, len(card_deck)):
            print("Index out of range")
        elif index in range(0, len(card_deck)) and card_name in card_deck:
            print("Card is already added")
        else:
            card_deck.insert(index, card_name)
            print("Card successfully added")

print(", ".join(card_deck))
