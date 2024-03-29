from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= 15

    def increase_oxygen(self, amount):
        self.oxygen += amount

