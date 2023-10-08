from project.core.drink_factory import DrinkFactory
from project.core.food_factory import FoodFactory
from project.core.table_factory import TableFactory
from project.core.validator import Validator


def find_entity_by_name(name, my_list):
    for x in my_list:
        if name == x.name:
            return x


def find_table_by_table_number(table_number, my_list):
    for x in my_list:
        if table_number == x.table_number:
            return x


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

        self.food_factory = FoodFactory()
        self.drink_factory = DrinkFactory()
        self.table_factory = TableFactory()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.is_empty_string_or_white_space(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        valid_types = ["Bread", "Cake"]
        if food_type in valid_types:
            if find_entity_by_name(name, self.food_menu):
                raise Exception(f"{food_type} {name} is already in the menu!")
            food = self.food_factory.create_a_food_instance(name, price, food_type)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        valid_types = ["Tea", "Water"]
        if drink_type in valid_types:
            if find_entity_by_name(name, self.drinks_menu):
                raise Exception(f"{drink_type} {name} is already in the menu!")
            drink = self.drink_factory.create_a_drink_instance(name, portion, brand, drink_type)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        valid_types = ["InsideTable", "OutsideTable"]
        if table_type in valid_types:
            if find_table_by_table_number(table_number, self.tables_repository):
                raise Exception(f"Table {table_number} is already in the bakery!")
            table = self.table_factory.create_a_table_instance(table_number, capacity, table_type)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        free_table = [x for x in self.tables_repository if not x.is_reserved and x.capacity >= number_of_people]
        if not free_table:
            return f"No available table for {number_of_people} people"
        free_table[0].reserve(number_of_people)
        return f"Table {free_table[0].table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *food_names):
        table = find_table_by_table_number(table_number, self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"
        result = [f"Table {table_number} ordered:\n"]
        missing = [f"{self.name} does not have in the menu:\n"]
        for name in food_names:
            food = find_entity_by_name(name, self.food_menu)
            if food:
                table.order_food(food)
                result.append(f"{food.__repr__()}\n")
            else:
                missing.append(f"{name}\n")
        result.extend(missing)
        return f"{''.join([x for x in result])}".strip()

    def order_drink(self, table_number, *drinks_name):
        table = find_table_by_table_number(table_number, self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"
        result = [f"Table {table_number} ordered:\n"]
        missing = [f"{self.name} does not have in the menu:\n"]
        for name in drinks_name:
            drink = find_entity_by_name(name, self.drinks_menu)
            if drink:
                table.order_drink(drink)
                result.append(f"{drink.__repr__()}\n")
            else:
                missing.append(f"{name}\n")
        result.extend(missing)
        return f"{''.join([x for x in result])}".strip()

    def leave_table(self, table_number):
        table = find_table_by_table_number(table_number, self.tables_repository)
        bill = table.get_bill()
        self.total_income += table.get_bill()
        table.clear()
        return f"Table: {table_number}\n"f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ""
        for x in self.tables_repository:
            if not x.is_reserved:
                result += f"{x.free_table_info()}\n"
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
