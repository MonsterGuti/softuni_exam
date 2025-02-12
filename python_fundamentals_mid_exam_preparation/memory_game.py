sequence_of_elements = input().split()
number_of_moves = 0

is_won = False
while sequence_of_elements:
    command = input()

    if command == "end":
        break

    user_indexes = command.split()
    first_index = int(user_indexes[0])
    second_index = int(user_indexes[1])
    number_of_moves += 1

    if first_index == second_index or first_index not in range(len(sequence_of_elements)) \
            or second_index not in range(len(sequence_of_elements)):

        middle_of_the_sequence = len(sequence_of_elements) // 2
        needed_element = f"-{number_of_moves}a"
        sequence_of_elements.insert(middle_of_the_sequence, needed_element)
        sequence_of_elements.insert(middle_of_the_sequence, needed_element)
        print("Invalid input! Adding additional elements to the board")
        continue

    if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        matched_element = sequence_of_elements[first_index]
        print(f"Congrats! You have found matching elements - {matched_element}!")

        for index in sorted([first_index, second_index], reverse=True):
            sequence_of_elements.pop(index)

        if not sequence_of_elements:
            print(f"You have won in {number_of_moves} turns!")
            is_won = True
            break
    else:
        print("Try again!")

if not is_won:
    print("Sorry you lose :(")
    print(" ".join(sequence_of_elements))
