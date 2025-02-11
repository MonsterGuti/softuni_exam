sequence_of_target = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break
    my_command = command.split()
    action = my_command[0]

    if action == "Shoot":
        index = int(my_command[1])
        power = int(my_command[2])
        if 0 <= index < len(sequence_of_target):
            sequence_of_target[index] -= power
            if sequence_of_target[index] <= 0:
                sequence_of_target.pop(index)

    elif action == "Add":
        index = int(my_command[1])
        value = int(my_command[2])
        if 0 <= index < len(sequence_of_target):
            sequence_of_target.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        index = int(my_command[1])
        radius = int(my_command[2])
        if 0 <= index - radius and index + radius < len(sequence_of_target):
            for target in range(index + radius, index, -1):
                sequence_of_target.pop(target)
            for target in range(index, index - radius - 1, -1):
                sequence_of_target.pop(target)

        else:
            print("Strike missed!")

print("|".join(map(str, sequence_of_target)))
