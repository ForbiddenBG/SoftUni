from collections import deque


fireworks_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

is_done = False

while fireworks_effects and explosive_power:
    first_firework = fireworks_effects[0]
    last_explosive = explosive_power[-1]
    if first_firework <= 0:
        fireworks_effects.popleft()
        continue
    if last_explosive <= 0:
        explosive_power.pop()
        continue
    result = first_firework + last_explosive
    if result % 3 == 0 and result % 5 != 0:
        fireworks["Palm Fireworks"] += 1
    elif result % 5 == 0 and result % 3 != 0:
        fireworks["Willow Fireworks"] += 1
    elif result % 3 == 0 and result % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    else:
        first_firework = fireworks_effects.popleft()
        first_firework -= 1
        fireworks_effects.append(first_firework)
        continue
    fireworks_effects.popleft()
    explosive_power.pop()
    if fireworks["Palm Fireworks"] >= 3 and\
            fireworks["Willow Fireworks"] >= 3 and\
            fireworks["Crossette Fireworks"] >= 3:
        is_done = True
        print("Congrats! You made the perfect firework show!")
        break

if not is_done:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for k, v in fireworks.items():
    print(f"{k}: {v}")
