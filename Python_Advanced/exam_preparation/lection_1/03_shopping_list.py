def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    # basket = set()
    products = []
    for product, product_data in kwargs.items():
        if len(products) == 5:
            break
        price = product_data[0]
        quantity = product_data[1]
        final_price = price * quantity

        if budget >= final_price:
            products.append(f"You bought {product} for {final_price:.2f} leva.")
            budget -= final_price

    return "\n".join(products)
