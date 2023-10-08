from abc import ABC, abstractmethod

from project.core.validator import Validator


class Astronaut(ABC):
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.is_empty_string_or_white_spaces(value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    @abstractmethod
    def increase_oxygen(self, amount):
        pass
