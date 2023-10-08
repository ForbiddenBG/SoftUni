from project.horse_race import HorseRace


class HorseRaceFactory:

    @staticmethod
    def creating_a_horse_race_instance(race_type):
        return HorseRace(race_type)
