initial_energy = int(input())

distance = input()
count_won_battles = 0
is_winner = True

while not distance == "End of the battle":
    distance = int(distance)
    if initial_energy - distance >= 0:
        initial_energy -= distance
        count_won_battles += 1
        if count_won_battles % 3 == 0:
            initial_energy += count_won_battles
    else:
        is_winner = False
        print(f"Not enough energy! Game ends with {count_won_battles} won battles and {initial_energy} energy")
        break

    distance = input()

if is_winner:
    print(f"Won battles: {count_won_battles}. Energy left: {initial_energy}")
