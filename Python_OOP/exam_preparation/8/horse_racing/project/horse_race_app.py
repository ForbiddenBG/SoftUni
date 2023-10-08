from project.core.horse_factory import HorseFactory
from project.core.horse_race_factory import HorseRaceFactory
from project.core.jockey_factory import JockeyFactory


def find_jockey_in_the_list_of_jockeys(name, my_list):
    for x in my_list:
        if name == x.name:
            return x


def find_horse_in_the_list_of_horses(horse_type, my_list):
    for index in range(len(my_list) - 1, -1, -1):
        horse = my_list[index]
        if horse.__class__.__name__ == horse_type and not horse.is_taken:
            return horse


def find_a_race(race_type, my_list):
    for x in my_list:
        if race_type == x.race_type:
            return x


def find_the_fastest_horse(participants):
    max_speed = -99999999
    jockey_name = ""
    horse_name = ""
    for x in participants:
        if x.horse.speed > max_speed:
            max_speed = x.horse.speed
            jockey_name = x.name
            horse_name = x.horse.name
    return max_speed, jockey_name, horse_name


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

        self.horse_factory = HorseFactory()
        self.horse_race_factory = HorseRaceFactory()
        self.jockey_factory = JockeyFactory()

    def add_horse(self, horse_type, horse_name, horse_speed):
        valid_horse_types = ["Appaloosa", "Thoroughbred"]
        if horse_type in valid_horse_types:
            for x in self.horses:
                if horse_name == x.name:
                    raise Exception(f"Horse {horse_name} has been already added!")
            horse = self.horse_factory.creating_a_horse(horse_name, horse_speed, horse_type)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        for x in self.jockeys:
            if jockey_name == x.name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = self.jockey_factory.creating_a_jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        for x in self.horse_races:
            if race_type == x.race_type:
                raise Exception(f"Race {race_type} has been already created!")
        race = HorseRaceFactory.creating_a_horse_race_instance(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        jockey = find_jockey_in_the_list_of_jockeys(jockey_name, self.jockeys)
        horse = find_horse_in_the_list_of_horses(horse_type, self.horses)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if horse and jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        jockey = find_jockey_in_the_list_of_jockeys(jockey_name, self.jockeys)
        race = find_a_race(race_type, self.horse_races)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if race and not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        race = find_a_race(race_type, self.horse_races)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        speed, jockey_name, horse_name = find_the_fastest_horse(race.jockeys)
        return f"The winner of the {race_type} race, with a speed of {speed}km/h is {jockey_name}! Winner's horse: {horse_name}."
