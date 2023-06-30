# Wrong output!

days = int(input())
players_count = int(input())
groups_energy = float(input())

water_per_person = float(input())
food_per_person = float(input())

total_water = water_per_person * players_count * days
total_food = food_per_person * players_count * days
is_over = False

for day in range(days):
    energy_loss = float(input())
    groups_energy -= energy_loss
    if groups_energy <= 0:
        is_over = True
        break
    if day % 2 == 0:
        groups_energy += groups_energy * 0.05
        total_water -= total_water * 0.30
    if day % 3 == 0:
        total_food -= total_food / players_count
        groups_energy += groups_energy * 0.10

if is_over:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")
