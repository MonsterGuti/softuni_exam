initial_treasure_chest = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break

    command = command.split()
    action = command[0]

    if action == "Loot":
        for item in command[1:]:
            if item not in initial_treasure_chest:
                initial_treasure_chest.insert(0, item)

    elif action == "Drop":
        index = int(command[1])
        if 0 <= index < len(initial_treasure_chest):
            initial_treasure_chest.append(initial_treasure_chest.pop(index))

    elif action == "Steal":
        count = int(command[1])
        count = min(count, len(initial_treasure_chest))
        stolen_items = initial_treasure_chest[-count:]
        del initial_treasure_chest[-count:]
        print(", ".join(stolen_items))

if initial_treasure_chest:
    average_treasure_gain = sum(len(item) for item in initial_treasure_chest) / len(initial_treasure_chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
