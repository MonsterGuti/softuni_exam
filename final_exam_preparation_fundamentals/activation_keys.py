activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    command_type = command.split(">>>")
    action = command_type[0]

    if action == "Contains":
        substring = command_type[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        case_type = command_type[1]
        start_index = int(command_type[2])
        end_index = int(command_type[3])

        if case_type == "Upper":
            activation_key = (
                activation_key[:start_index] +
                activation_key[start_index:end_index].upper() +
                activation_key[end_index:]
            )
        elif case_type == "Lower":
            activation_key = (
                activation_key[:start_index] +
                activation_key[start_index:end_index].lower() +
                activation_key[end_index:]
            )
        print(activation_key)

    elif action == "Slice":
        start_index = int(command_type[1])
        end_index = int(command_type[2])

        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")
