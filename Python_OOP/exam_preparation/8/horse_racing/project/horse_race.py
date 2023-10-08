from project.core.Validator import Validator


class HorseRace:
    VALID_HORSE_RACES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        Validator.the_race_type_is_not_in_the_available_races(value, HorseRace.VALID_HORSE_RACES, "Race type does not exist!")
        self.__race_type = value
