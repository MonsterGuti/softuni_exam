initial_energy = int(input())
won_battles = 0
energy_left = initial_energy
is_failed = False

while True:
    command = input()
    if command == "End of battle":
        break
    distance = int(command)
    if energy_left < distance:
        is_failed = True
        break
    energy_left -= distance
    won_battles += 1
    if won_battles % 3 == 0:
        energy_left += won_battles
if is_failed:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy_left} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {energy_left}")
