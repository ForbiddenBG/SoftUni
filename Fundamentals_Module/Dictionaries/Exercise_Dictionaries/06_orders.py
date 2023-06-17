data = input()

products = {}
# products_prices {}
# products_quantities = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    # if name not in products_prices:
    #     products_prices[name] = price
    #     products_quantities[name] = quantity
    # else:
    #     products_prices[name] = price
    #     products_quantities[name] += quantity

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price

    data = input()

# for product, price in products_prices.items():
#     result = price * products_quantities[product]
#     print(f"{product} -> {result:.2f}")

for key, value in products.items():
    result = value["price"] * value["quantity"]
    print(f"{key} -> {result:.2f}")


# data = input()
#
# products = {}
#
# while not data == "buy":
#     name, price, quantity = data.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if name not in products:
#         products[name] = []
#         products[name].append(price)
#         products[name].append(quantity)
#     else:
#         products[name][1] += quantity
#         if not products[name][0] == price:
#             products[name].pop(0)
#             products[name].insert(0, price)
#
#     data = input()
#
# for k, v in products.items():
#     print(f"{k} -> {(v[0] * v[1]):.2f}")

