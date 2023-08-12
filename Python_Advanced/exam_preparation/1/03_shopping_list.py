def shopping_list(budget, **kwargs):
    basket = []
    count = 5
    if budget < 100:
        return "You do not have enough budget."
    elif budget >= 100:
        for product, value in kwargs.items():
            price, quantity = (float(x) for x in value)
            needed_money = price * quantity
            if budget >= needed_money:
                budget -= needed_money
                basket.append(f"You bought {product} for {price * quantity:.2f} leva.")
                count -= 1
                if count == 0:
                    break
    return "\n".join(basket)


# def shopping_list(budget, **kwargs):
#     basket = []
#     result = ""
#
#     if budget >= 100:
#         for product, tup in kwargs.items():
#             if len(basket) != 5 and kwargs.values() != 0:
#                 product_price = float(tup[0])
#                 quantity = tup[1]
#                 total_cost = product_price * quantity
#                 if budget >= total_cost:
#                     budget -= total_cost
#                     kwargs[product] = 0
#                     basket.append(product)
#                     result += f"You bought {product} for {total_cost:.2f} leva." + "\n"
#             else:
#                 break
#     else:
#         return "You do not have enough budget."
#
#     return result.strip()


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
