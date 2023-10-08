from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    @property
    def max_horse_speed(self):
        return 120

    def train(self):
        if self.speed + 2 > self.max_horse_speed:
            self.speed = self.max_horse_speed
        else:
            self.speed += 2
