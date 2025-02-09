people_waiting = int(input())
people_left = people_waiting
maximum_capacity = 4
number_of_waggons = list(map(int, input().split()))

for i in range(len(number_of_waggons)):
    current_waggon_seats = number_of_waggons[i]
    available_seats = maximum_capacity - current_waggon_seats

    if people_left >= available_seats:
        number_of_waggons[i] += available_seats
        people_left -= available_seats
    else:
        number_of_waggons[i] += people_left
        people_left = 0

final_string = " ".join(map(str, number_of_waggons))

if people_left > 0:
    print(f"There isn't enough space! {people_left} people in a queue!")
    print(final_string)
elif any(seats < maximum_capacity for seats in number_of_waggons):
    print("The lift has empty spots!")
    print(final_string)
else:
    print(final_string)
