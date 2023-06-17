legendary_item = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
my_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
is_obtained = False


data = input()
while not is_obtained:
    couple = data.split()
    for i in range(0, len(couple), 2):
        quantity = int(couple[i])
        material = couple[i + 1].lower()

        if material in my_dict:
            my_dict[material] += quantity
            if my_dict[material] >= 250:
                my_dict[material] -= 250
                is_obtained = True
                print(f"{legendary_item[material]} obtained!")
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

    if is_obtained:
        break

    data = input()

sorted_remaining_materials = sorted(my_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))
sorted_junk = sorted(junk.items(), key=lambda kvp: kvp[0])

for k, v in sorted_remaining_materials:
    print(f"{k}: {v}")
for k, v in sorted_junk:
    print(f"{k}: {v}")
