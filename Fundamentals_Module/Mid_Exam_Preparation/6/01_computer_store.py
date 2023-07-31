price = 0
taxes = 0
total_price = 0
is_valid = False

command = input()
while True:
    if command == "special":
        is_valid = True
        break
    elif command == "regular":
        break
    else:
        command = float(command)
        if command < 0:
            print(f"Invalid price!")
        else:
            price += command
            taxes += command * 0.2
    command = input()

if is_valid:
    total_price = price + taxes - ((price + taxes) * 0.1)
else:
    total_price = price + taxes

if total_price == 0:
    print(f"Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
