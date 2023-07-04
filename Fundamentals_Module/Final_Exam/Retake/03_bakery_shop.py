my_dict = {}
count_sold = 0

command = input()
while not command == "Complete":
    main_data = command.split()
    if main_data[0] == "Receive":
        quantity, food = main_data[1:]
        quantity = int(quantity)
        if quantity > 0:
            if food not in my_dict:
                my_dict[food] = quantity
            else:
                my_dict[food] += quantity
    elif main_data[0] == "Sell":
        quantity, food = main_data[1:]
        quantity = int(quantity)
        if food not in my_dict:
            print(f"You do not have any {food}.")
        else:
            if my_dict[food] < quantity:
                sold = my_dict[food]
                count_sold += sold
                del my_dict[food]
                print(f"There aren't enough {food}. You sold the last {sold} of them.")
            elif my_dict[food] >= quantity:
                my_dict[food] -= quantity
                count_sold += quantity
                print(f"You sold {quantity} {food}.")
                if my_dict[food] == 0:
                    del my_dict[food]
    command = input()

sorted_food = sorted(my_dict.items(), key=lambda kvp: kvp[0])

for k, v in sorted_food:
    print(f"{k}: {v}")
print(f"All sold: {count_sold} goods")
