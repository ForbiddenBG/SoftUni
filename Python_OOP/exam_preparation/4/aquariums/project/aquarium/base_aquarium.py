from abc import ABC

from project.core.validator import Validator


class BaseAquarium(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_it_is_an_empty_string(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([x.comfort for x in self.decorations])

    def add_fish(self, fish):
        valid_types = ["FreshwaterFish", "SaltwaterFish"]
        if fish.__class__.__name__ in valid_types:
            if self.capacity == len(self.fish):
                return f"Not enough capacity."
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.capacity += fish.size
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if self.fish:
            result += f"Fish: {' '.join([fish.name for fish in self.fish])}\n"
        else:
            result += "Fish: none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result.strip()
