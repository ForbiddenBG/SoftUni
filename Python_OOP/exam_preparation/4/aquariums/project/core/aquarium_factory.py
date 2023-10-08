from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium


class AquariumFactory:
    valid_types = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}

    @staticmethod
    def create_an_aquarium_object(name, aquarium_type):
        return AquariumFactory.valid_types[aquarium_type](name)
