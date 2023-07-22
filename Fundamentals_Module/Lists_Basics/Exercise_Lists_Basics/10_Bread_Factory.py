events = input().split("|")

energy = 100
coins = 100
is_closed = False

for event in events:
    main_event = event.split("-")
    event_name = main_event[0]
    event_value = int(main_event[1])

    if event_name == "rest":
        if energy + event_value <= 100:
            energy += event_value
            print(f"You gained {event_value} energy.")
        else:
            print("You gained 0 energy.")
        print(f"Current energy: {energy}.")
    elif event_name == "order":
        if energy - 30 >= 0:
            coins += event_value
            energy -= 30
            print(f"You earned {event_value} coins.")
        elif energy - 30 < 0:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins > event_value:
            coins -= event_value
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            is_closed = True
            break

if not is_closed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
