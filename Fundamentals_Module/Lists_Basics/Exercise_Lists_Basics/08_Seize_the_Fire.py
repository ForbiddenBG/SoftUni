level_of_fire = input().split("#")
amount_of_water = int(input())

effort = 0
total_fire = 0
my_list = []

for fire in level_of_fire:
    cell = str(fire).split(" = ")
    fire_type = cell[0]
    fire_range = int(cell[1])

    if fire_type == "High":
        if 81 <= fire_range <= 125 and amount_of_water >= fire_range:
            amount_of_water -= fire_range
            effort += (fire_range * 0.25)
            total_fire += fire_range
            my_list.append(fire_range)
    elif fire_type == "Medium":
        if 51 <= fire_range <= 80 and amount_of_water >= fire_range:
            amount_of_water -= fire_range
            effort += (fire_range * 0.25)
            total_fire += fire_range
            my_list.append(fire_range)
    elif fire_type == "Low":
        if 1 <= fire_range <= 50 and amount_of_water >= fire_range:
            amount_of_water -= fire_range
            effort += (fire_range * 0.25)
            total_fire += fire_range
            my_list.append(fire_range)
print("Cells:")
for siezed in my_list:
    print(f"- {siezed}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
