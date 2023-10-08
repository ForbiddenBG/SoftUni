from abc import ABC, abstractmethod

from project.core.Validator import Validator


class Car(ABC):
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.the_model_is_less_than_four_symbols(
            value, f"Model {value} is less than 4 symbols!"
        )
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.the_speed_is_out_of_the_valid_range(
            value,
            f"Invalid speed limit! Must be between"
            f" {self.min_speed} and {self.max_speed}!",
            self.min_speed, self.max_speed
        )
        self.__speed_limit = value

    @property
    @abstractmethod
    def min_speed(self):
        pass

    @property
    @abstractmethod
    def max_speed(self):
        pass
