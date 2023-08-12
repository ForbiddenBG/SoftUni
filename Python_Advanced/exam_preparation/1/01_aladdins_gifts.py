from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic_level:
    last_material = materials.pop()
    first_magic = magic_level.popleft()
    result = last_material + first_magic
    if result < 100:
        if result % 2 == 0:
            result = (last_material * 2) + (first_magic * 3)
        else:
            result *= 2
    if result > 499:
        result /= 2
    if 100 <= result <= 199:
        presents['Gemstone'] += 1
    elif 200 <= result <= 299:
        presents['Porcelain Sculpture'] += 1
    elif 300 <= result <= 399:
        presents['Gold'] += 1
    elif 400 <= result <= 499:
        presents['Diamond Jewellery'] += 1

if (presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0) or\
        (presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for k, v in sorted(presents.items()):
    if v > 0:
        print(f"{k}: {v}")
