from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarFactory:
    valid_car_types = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    @staticmethod
    def creating_a_car_instance(car_type,  model, speed):
        if car_type in CarFactory.valid_car_types:
            return CarFactory.valid_car_types[car_type](model, speed)
