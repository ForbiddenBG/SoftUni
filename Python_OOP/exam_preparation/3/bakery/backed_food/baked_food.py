from abc import ABC, abstractmethod

from project.core.validator import Validator


class BakedFood(ABC):
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.is_empty_string_or_white_space(value, "Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.if_is_equal_or_less_than_0(value, "Price cannot be less than or equal to zero!")
        self.__price = value

    @abstractmethod
    def __repr__(self):
        pass
