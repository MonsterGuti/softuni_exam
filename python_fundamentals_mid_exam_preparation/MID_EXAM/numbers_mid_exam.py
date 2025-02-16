numbers_sequence = list(map(int, input().split()))
while True:
    command = input()
    if command == "Finish":
        break

    command_type = command.split()
    action = command_type[0]
    value = int(command_type[1])

    if action == "Add":
        numbers_sequence.append(value)
    elif action == "Remove":
        numbers_sequence.remove(value)
    elif action == "Replace":
        replacement = int(command_type[2])
        if value in numbers_sequence:
            my_index = numbers_sequence.index(value)
            numbers_sequence.pop(my_index)
            numbers_sequence.insert(my_index, replacement)
    elif action == "Collapse":
        numbers_sequence = list(num for num in numbers_sequence if num >= value)

print(" ".join(map(str, numbers_sequence)))
