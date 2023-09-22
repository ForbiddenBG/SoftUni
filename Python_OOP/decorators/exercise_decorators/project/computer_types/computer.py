from abc import ABC, abstractmethod

from Python_OOP.decorators.exercise_decorators.project.core.validator import Validator


class Computer(ABC):
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0
        
    @property
    def manufacturer(self):
        return self.__manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        Validator.raise_if_the_string_is_enmpty_or_whitespace(value, "Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.raise_if_the_string_is_enmpty_or_whitespace(value, "Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor, ram):
        pass

    def __repr__(self):
        return f"{ self.manufacturer } { self.model } with { self.processor } and { self.ram }GB RAM"
