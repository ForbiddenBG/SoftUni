from abc import ABC
from project.core.validator import Validator


class Supply(ABC):
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        Validator.energy_is_less_than_zero(value, "Energy cannot be less than zero.")
        self.__energy = value

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
