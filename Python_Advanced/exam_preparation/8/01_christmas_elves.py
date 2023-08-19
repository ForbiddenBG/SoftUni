from collections import deque

elfs_energy = deque([int(x) for x in input().split()])
materials_in_boxes = [int(x) for x in input().split()]

toys = 0
used_energy = 0
turns = 0

while elfs_energy and materials_in_boxes:
    current_toys = 0
    turns += 1
    first_elf = elfs_energy.popleft()
    last_box = materials_in_boxes[-1]

    if first_elf < 5:
        turns -= 1
        continue

    if last_box > first_elf:
        first_elf = first_elf*2
        elfs_energy.append(first_elf)
        continue

    if first_elf >= last_box and turns % 3 != 0:
        first_elf -= last_box
        used_energy += last_box
        current_toys += 1
        first_elf += 1

    if turns % 3 == 0:
        if first_elf >= last_box*2:
            current_toys += 2
            first_elf -= last_box*2
            used_energy += last_box*2
            first_elf += 1

        elif last_box*2 > first_elf:
            first_elf = first_elf*2
            elfs_energy.append(first_elf)
            continue

    if turns % 5 == 0:
        current_toys -= current_toys
        first_elf -= 1

    toys += current_toys
    elfs_energy.append(first_elf)
    materials_in_boxes.pop()

print(f"Toys: {toys}")
print(f"Energy: {used_energy}")
if elfs_energy:
    print(f"Elves left: {', '.join([str(x) for x in elfs_energy])}")
if materials_in_boxes:
    print(f"Boxes left: {', '.join([str(x) for x in materials_in_boxes])}")
