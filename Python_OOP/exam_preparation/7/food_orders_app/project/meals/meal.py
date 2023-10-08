from abc import ABC, abstractmethod
from project.core.Validator import Validator


class Meal(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raises_if_the_value_is_empty_string(value, "Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raises_if_the_value_is_less_than_or_equal_to_zero(value, "Invalid price!")
        self.__price = value

    @abstractmethod
    def details(self):
        pass
