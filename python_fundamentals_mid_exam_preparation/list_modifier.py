numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == "swap":
        f_index = int(command_parts[1])
        s_index = int(command_parts[2])
        numbers[f_index], numbers[s_index] = numbers[s_index], numbers[f_index]

    elif action == "multiply":
        f_index = int(command_parts[1])
        s_index = int(command_parts[2])
        numbers[f_index] *= numbers[s_index]

    elif action == "decrease":
        numbers = [num - 1 for num in numbers]

print(", ".join(map(str, numbers)))
