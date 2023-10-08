from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseFactory:
    available_types = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def creating_a_horse(self, name, horse_speed, horse_type):
        if horse_type in HorseFactory.available_types:
            horse = self.available_types[horse_type](name, horse_speed)
            return horse
