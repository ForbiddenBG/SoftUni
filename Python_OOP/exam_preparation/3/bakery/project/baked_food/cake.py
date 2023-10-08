from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    def __init__(self, name, price):
        super().__init__(name, 245, price)

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
