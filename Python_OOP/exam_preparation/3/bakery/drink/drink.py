from abc import ABC, abstractmethod

from project.core.validator import Validator


class Drink(ABC):
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.is_empty_string_or_white_space(value, "Name cannot be empty string or white space!")
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        Validator.if_is_equal_or_less_than_0(value, "Portion cannot be less than or equal to zero!")
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validator.is_empty_string_or_white_space(value, "Brand cannot be empty string or white space!")
        self.__brand = value

    @abstractmethod
    def __repr__(self):
        pass
