number = int(input())

heroes = {}

for _ in range(number):
    hero_name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    heroes[hero_name] = {"hit_points": hp, "mana_points": mp}

command = input()
while not command == "End":
    main_data = command.split(" - ")

    if main_data[0] == "CastSpell":
        hero_name, mp_needed, spell_name = main_data[1:]
        mp_needed = int(mp_needed)
        if heroes[hero_name]["mana_points"] >= mp_needed:
            heroes[hero_name]["mana_points"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana_points']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif main_data[0] == "TakeDamage":
        hero_name, damage, attacker = main_data[1:]
        damage = int(damage)
        if heroes[hero_name]['hit_points'] - damage > 0:
            heroes[hero_name]['hit_points'] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hit_points']} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif main_data[0] == "Recharge":
        hero_name, amount = main_data[1:]
        amount = int(amount)
        if heroes[hero_name]['mana_points'] + amount <= 200:
            heroes[hero_name]['mana_points'] += amount
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['mana_points']} MP!")
            heroes[hero_name]['mana_points'] = 200

    elif main_data[0] == "Heal":
        hero_name, amount = main_data[1:]
        amount = int(amount)
        if heroes[hero_name]['hit_points'] + amount <= 100:
            heroes[hero_name]['hit_points'] += amount
            print(f"{hero_name} healed for {amount} HP!")
        else:
            print(f"{hero_name} healed for {100 - heroes[hero_name]['hit_points']} HP!")
            heroes[hero_name]['hit_points'] = 100

    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda kvpt: (-kvpt[1]['hit_points'], kvpt[0]))

for k, v in sorted_heroes:
    print(f"{k}")
    print(f"  HP: {v['hit_points']}")
    print(f"  MP: {v['mana_points']}")
