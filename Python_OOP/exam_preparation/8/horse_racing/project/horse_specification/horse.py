from abc import ABC, abstractmethod
from project.core.Validator import Validator


class Horse(ABC):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.the_string_len_is_under_four_symbols(value, f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.the_speed_exceeded_the_max_speed(value, self.max_horse_speed, "Horse speed is too high!")
        self.__speed = value

    @property
    @abstractmethod
    def max_horse_speed(self):
        pass

    @abstractmethod
    def train(self):
        pass
