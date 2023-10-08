from project.core.ClientFactory import ClientFactory
from copy import copy


def find_client_by_phone(phone, my_list):
    for x in my_list:
        if phone == x.phone_number:
            return x


def reversing_the_quantities_in_the_menu(shopping_cart, menu):
    for x in shopping_cart:
        for j in menu:
            if x.name == j.name:
                j.quantity += x.quantity
    return menu


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.order_id = 0
        self.client_factory = ClientFactory()

    def register_client(self, client_phone_number):
        for client in self.clients_list:
            if client_phone_number == client.phone_number:
                raise Exception("The client has already been registered!")
        client = ClientFactory.create_a_client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ == "Starter":
                self.menu.append(meal)
            if meal.__class__.__name__ == "MainDish":
                self.menu.append(meal)
            if meal.__class__.__name__ == "Dessert":
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = ""
        for meal in self.menu:
            result += f"{meal.details()}\n"
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        client_x = find_client_by_phone(client_phone_number, self.clients_list)
        if not client_x:
            FoodOrdersApp.register_client(self, client_phone_number)
            client_x = find_client_by_phone(client_phone_number, self.clients_list)

        for name, quantity in meal_names_and_quantities.items():
            is_found = False
            if len(self.menu) < 5:
                raise Exception("The menu is not ready!")
            for meal in self.menu:
                if name == meal.name:
                    is_found = True
                    if meal.quantity >= quantity:
                        meal.quantity -= quantity
                        client_x.bill += meal.price * quantity
                        ordered_meal = copy(meal)
                        ordered_meal.quantity = quantity
                        client_x.shopping_cart.append(ordered_meal)
                        break
                    self.menu = reversing_the_quantities_in_the_menu(client_x.shopping_cart, self.menu)
                    client_x.bill = 0
                    client_x.shopping_cart = []
                    raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")
            if is_found:
                continue
            self.menu = reversing_the_quantities_in_the_menu(client_x.shopping_cart, self.menu)
            client_x.bill = 0
            client_x.shopping_cart.clear()
            raise Exception(f"{name} is not on the menu!")
        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join([x.name for x in client_x.shopping_cart])} for {client_x.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = find_client_by_phone(client_phone_number, self.clients_list)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        self.menu = reversing_the_quantities_in_the_menu(client.shopping_cart, self.menu)
        client.bill = 0
        client.shopping_cart.clear()
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = find_client_by_phone(client_phone_number, self.clients_list)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        client.shopping_cart.clear()
        current_bill = client.bill
        client.bill = 0
        self.order_id += 1
        return f"Receipt #{self.order_id} with total amount of {current_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
