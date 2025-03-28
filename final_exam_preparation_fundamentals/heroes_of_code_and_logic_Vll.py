def cast_spell(my_heroes_dict, some_command):
    split_command = some_command.split(" - ")
    current_hero_name = split_command[1]
    mp_needed = split_command[2]
    spell_name = split_command[3]
    mp_needed = int(mp_needed)

    if my_heroes_dict[current_hero_name]["mp"] >= mp_needed:
        my_heroes_dict[current_hero_name]["mp"] -= mp_needed
        mana_points_left = my_heroes_dict[current_hero_name]["mp"]
        print(f"{current_hero_name} has successfully cast {spell_name} and now has {mana_points_left} MP!")
    else:
        print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(my_heroes_dict, some_command):
    split_command = some_command.split(" - ")
    current_hero_name = split_command[1]
    damage = int(split_command[2])
    attacker = split_command[3]

    my_heroes_dict[current_hero_name]["hp"] -= damage
    if my_heroes_dict[current_hero_name]["hp"] > 0:
        current_hp = my_heroes_dict[current_hero_name]["hp"]
        print(f"{current_hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
    else:
        del my_heroes_dict[current_hero_name]
        print(f"{current_hero_name} has been killed by {attacker}!")


def recharge(my_heroes_dict, some_command, max_mp):
    split_command = some_command.split(" - ")
    current_hero_name = split_command[1]
    amount = int(split_command[2])

    if my_heroes_dict[current_hero_name]["mp"] + amount > max_mp:
        amount_recovered = max_mp - my_heroes_dict[current_hero_name]["mp"]
        my_heroes_dict[current_hero_name]["mp"] = max_mp
    else:
        amount_recovered = amount
        my_heroes_dict[current_hero_name]["mp"] += amount

    print(f"{current_hero_name} recharged for {amount_recovered} MP!")


def heal(my_heroes_dict, some_command, max_hp):
    split_command = some_command.split(" - ")
    current_hero_name = split_command[1]
    amount = int(split_command[2])

    if my_heroes_dict[current_hero_name]["hp"] + amount > max_hp:
        amount_recovered = max_hp - my_heroes_dict[current_hero_name]["hp"]
        my_heroes_dict[current_hero_name]["hp"] = max_hp
    else:
        amount_recovered = amount
        my_heroes_dict[current_hero_name]["hp"] += amount

    print(f"{current_hero_name} healed for {amount_recovered} HP!")


maximum_mp = 200
maximum_hp = 100

number_of_heroes = int(input())
heroes_dict = {}

for _ in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    heroes_dict[hero_name] = {"hp": int(hp), "mp": int(mp)}

while True:
    command = input()
    if command == "End":
        break

    action = command.split(" - ")[0]

    if action == "CastSpell":
        cast_spell(heroes_dict, command)
    elif action == "TakeDamage":
        take_damage(heroes_dict, command)
    elif action == "Recharge":
        recharge(heroes_dict, command, maximum_mp)
    elif action == "Heal":
        heal(heroes_dict, command, maximum_hp)

for hero, points in heroes_dict.items():
    print(f"{hero}\n  HP: {points['hp']}\n  MP: {points['mp']}")
