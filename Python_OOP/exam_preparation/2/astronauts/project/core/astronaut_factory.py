from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautFactory:
    valid_types = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    @staticmethod
    def creating_an_astronaut_instance(astronaut_type, name):
        if astronaut_type in AstronautFactory.valid_types:
            return AstronautFactory.valid_types[astronaut_type](name)
