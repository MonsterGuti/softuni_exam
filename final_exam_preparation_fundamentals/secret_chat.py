secret_message = input()
encrypted_message = ""
while True:
    command = input()
    if command == "Reveal":
        break

    command_type = command.split(":|:")
    action = command_type[0]

    if action == "InsertSpace":
        index = int(command_type[1])
        secret_message = secret_message[:index] + " " + secret_message[index:]
        print(secret_message)

    elif action == "Reverse":
        substring = command_type[1]
        if substring in secret_message:
            reversed_substring = substring[::-1]
            secret_message = secret_message.replace(substring, "", 1)
            secret_message += reversed_substring
            print(secret_message)
        else:
            print("error")
            continue

    elif action == "ChangeAll":
        substring = command_type[1]
        replacement = command_type[2]
        secret_message = secret_message.replace(substring, replacement)
        print(secret_message)

print(f"You have a new text message: {secret_message}")
