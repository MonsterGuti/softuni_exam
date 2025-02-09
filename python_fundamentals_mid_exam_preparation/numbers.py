space_separated_integers = list(map(int, input().split()))
avg_num = sum(space_separated_integers) / len(space_separated_integers)
greater_numbers = list(num for num in space_separated_integers if num > avg_num)
printed_numbers = 5

if not greater_numbers:
    print("No")

if len(greater_numbers) < printed_numbers:
    greater_numbers.sort(reverse=True)
    for n in greater_numbers:
        print(n, end=" ")

else:
    greater_numbers.sort(reverse=True)
    elements = 0

    for n in greater_numbers:
        print(n, end=" ")
        elements += 1

        if elements == 5:
            break
