from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    @property
    def max_horse_speed(self):
        return 140

    def train(self):
        if self.speed + 3 > self.max_horse_speed:
            self.speed = self.max_horse_speed
        else:
            self.speed += 3
