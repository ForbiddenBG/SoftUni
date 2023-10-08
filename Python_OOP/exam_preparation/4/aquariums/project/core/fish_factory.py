from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class FishFactory:
    valid_types = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    @staticmethod
    def create_a_fish_object(fish_name, fish_species, fish_price, fish_type):
        return FishFactory.valid_types[fish_type](fish_name, fish_species, fish_price)
