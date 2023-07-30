health = 100
bitcoins = 0
data = input().split("|")

room = 0
is_dead = False

while not health <= 0 and room < len(data):
    for h in data:
        final = h.split()
        command = final[0]
        number = int(final[1])
        room += 1
        if command == "potion":
            if 0 < health < 100:
                if number + health > 100:
                    rest = 100 - health
                    health += (100 - health)
                    print(f'You healed for {rest} hp.')
                    print(f"Current health: {health} hp.")
                else:
                    health += number
                    print(f'You healed for {number} hp.')
                    print(f"Current health: {health} hp.")
        elif command == "chest":
            bitcoins += number
            print(f"You found {number} bitcoins.")
        else:
            health -= number
            if not health <= 0:
                print(f"You slayed {command}.")
            else:
                print(f"You died! Killed by {command}.")
                print(f"Best room: {room}")
                is_dead = True
                break
        if is_dead:
            break
    if is_dead:
        break


if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
