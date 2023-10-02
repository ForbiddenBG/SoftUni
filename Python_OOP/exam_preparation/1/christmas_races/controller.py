from project.core.car_factory import CarFactory
from project.core.driver_factory import DriverFactory
from project.core.race_factory import RaceFactory


def find_driver_by_name(driver_name, my_list):
    for driver in my_list:
        if driver_name == driver.name:
            return driver


def find_race_by_name(race_name, my_list):
    for race in my_list:
        if race_name == race.name:
            return race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

        self.car_factory = CarFactory()
        self.driver_factory = DriverFactory()
        self.race_factory = RaceFactory()

    def create_car(self, car_type, model, speed_limit):
        valid_car_types = ["MuscleCar", "SportsCar"]
        if car_type in valid_car_types:
            for x in self.cars:
                if x.model == model:
                    raise Exception(f"Car {model} is already created!")
            car = self.car_factory.creating_a_car_instance(car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        driver = find_driver_by_name(driver_name, self.drivers)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")
        driver_obj = self.driver_factory.creating_a_driver_instance(driver_name)
        self.drivers.append(driver_obj)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        race = find_race_by_name(race_name, self.races)
        if race:
            raise Exception(f"Race {race_name} is already created!")
        race_obj = self.race_factory.creating_a_race_instance(race_name)
        self.races.append(race_obj)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        car_list = [x for x in self.cars if car_type == x.__class__.__name__]
        driver = find_driver_by_name(driver_name, self.drivers)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not car_list or not [x for x in car_list if not x.is_taken]:
            raise Exception(f"Car {car_type} could not be found!")
        last_free_car = [x for x in car_list if not x.is_taken][-1]
        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = last_free_car
            last_free_car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {last_free_car.model}."
        if not driver.car:
            driver.car = last_free_car
            last_free_car.is_taken = True
            return f"Driver {driver_name} chose the car {last_free_car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        driver = find_driver_by_name(driver_name, self.drivers)
        race = find_race_by_name(race_name, self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if race and not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if race and driver.car and driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = find_race_by_name(race_name, self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        drivers_list = [x for x in race.drivers]
        fastest_sorted = sorted(reversed(drivers_list), key=lambda x: -x.car.speed_limit)
        fastest_three = [x for x in fastest_sorted][:3]

        result = ""
        for x in fastest_three:
            x.number_of_wins += 1
            result += f"Driver {x.name} wins the {race_name} race with a speed of {x.car.speed_limit}.\n"
        return result.strip()
