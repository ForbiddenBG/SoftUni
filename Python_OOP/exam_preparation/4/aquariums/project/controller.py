from project.core.aquarium_factory import AquariumFactory
from project.core.decoration_factory import DecorationFactory
from project.core.fish_factory import FishFactory
from project.decoration.decoration_repository import DecorationRepository


def find_aquarium_by_name(aquarium_name, my_list):
    for aqua in my_list:
        if aquarium_name == aqua.name:
            return aqua


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

        self.aquarium_factory = AquariumFactory()
        self.decoration_factory = DecorationFactory()
        self.fish_factory = FishFactory()

    def add_aquarium(self, aquarium_type, aquarium_name):
        valid_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type in valid_types:
            aquarium = self.aquarium_factory.create_an_aquarium_object(aquarium_name, aquarium_type)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type):
        valid_types = ["Ornament", "Plant"]
        if decoration_type in valid_types:
            decoration = self.decoration_factory.create_a_decoration_object(decoration_type)
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name, decoration_type):
        aquarium = find_aquarium_by_name(aquarium_name, self.aquariums)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."
        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        valid_types = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type in valid_types:
            fish = self.fish_factory.create_a_fish_object(fish_name, fish_species, price, fish_type)
            aquarium = find_aquarium_by_name(aquarium_name, self.aquariums)
            if fish.VALID_HABITAT != aquarium.__class__.__name__:
                return "Water not suitable."
            return aquarium.add_fish(fish)
        return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name):
        aquarium = find_aquarium_by_name(aquarium_name, self.aquariums)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = find_aquarium_by_name(aquarium_name, self.aquariums)
        total_value = sum(x.price for x in aquarium.decorations) + sum(x.price for x in aquarium.fish)
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        result = ""
        for aqua in self.aquariums:
            result += f"{aqua.__str__()}\n"
        return result.strip()
