from project.baked_food.bread import Bread
from project.baked_food.cake import Cake


class FoodFactory:

    valid_types = {"Bread": Bread, "Cake": Cake}

    @staticmethod
    def create_a_food_instance(name, price, food_type):
        return FoodFactory.valid_types[food_type](name, price)

