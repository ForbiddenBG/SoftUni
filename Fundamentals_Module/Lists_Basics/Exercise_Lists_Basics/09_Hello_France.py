collection_of_items = input().split("|")
budget = float(input())
train_ticket = 150

bought_items_prices = []
sold_items_cost = 0
profit = 0

for item in collection_of_items:
    new_item = item.split("->")
    item_type = new_item[0]
    item_price = float(new_item[1])

    if item_type == "Clothes" and item_price <= 50.00 and budget - item_price >= 0:
        budget -= item_price
        sold_items_cost += item_price * 1.4
        profit += item_price * 0.40
        bought_items_prices.append(f"{(item_price * 1.4):.2f}")
    elif item_type == "Shoes" and item_price <= 35.00 and budget - item_price >= 0:
        budget -= item_price
        sold_items_cost += item_price * 1.4
        profit += item_price * 0.40
        bought_items_prices.append(f"{(item_price * 1.4):.2f}")
    elif item_type == "Accessories" and item_price <= 20.50 and budget - item_price >= 0:
        budget -= item_price
        sold_items_cost += item_price * 1.4
        profit += item_price * 0.40
        bought_items_prices.append(f"{(item_price * 1.4):.2f}")
    else:
        continue

for item in bought_items_prices:
    item = float(item)
    print(f"{item:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

if sold_items_cost + budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
