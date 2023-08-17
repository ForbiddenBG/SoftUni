def shopping_cart(*args):
    products = {"Soup": [], "Pizza": [], "Dessert": []}

    for data in args:
        if data == "Stop" and products["Soup"] == [] and products["Pizza"] == [] and products["Dessert"] == []:
            return "No products in the cart!"
        if data == "Stop":
            result = ""
            sorted_meals = sorted(products.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
            for k, v in sorted_meals:
                result += f"{k}:" + "\n"
                for x in sorted(v):
                    result += f" - {x}" + "\n"
            return result.strip()

        meal, ingredients = data[0], data[1]
        if len(products["Soup"]) < 3 and meal == "Soup" and ingredients not in products["Soup"]:
            products[meal].append(ingredients)
        if len(products["Pizza"]) < 4 and meal == "Pizza" and ingredients not in products["Pizza"]:
            products[meal].append(ingredients)
        if len(products["Dessert"]) < 2 and meal == "Dessert" and ingredients not in products["Dessert"]:
            products[meal].append(ingredients)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
