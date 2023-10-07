from project.drink.tea import Tea
from project.drink.water import Water


class DrinkFactory:

    valid_types = {"Tea": Tea, "Water": Water}

    @staticmethod
    def create_a_drink_instance(name, portion, brand, drink_type):
        return DrinkFactory.valid_types[drink_type](name, portion, brand)
