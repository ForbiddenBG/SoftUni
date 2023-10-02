from project.race import Race


class RaceFactory:

    @staticmethod
    def creating_a_race_instance(race_name):
        return Race(race_name)
