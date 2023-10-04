from project.astronaut.astronaut_repository import AstronautRepository
from project.core.astronaut_factory import AstronautFactory
from project.core.planet_factory import PlanetFactory
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.astronaut_factory = AstronautFactory()
        self.planet_factory = PlanetFactory()
        self.missions_compleated = 0
        self.missions_not_compleated = 0

    def add_astronaut(self, astronaut_type, name):
        valid_types = ["Biologist", "Geodesist", "Meteorologist"]
        if astronaut_type in valid_types:
            astronaut = self.astronaut_repository.find_by_name(name)
            if astronaut in self.astronaut_repository.astronauts:
                return f"{name} is already added."
            astronaut_obj = self.astronaut_factory.creating_an_astronaut_instance(astronaut_type, name)
            self.astronaut_repository.add(astronaut_obj)
            return f"Successfully added {astronaut_type}: {name}."
        raise Exception("Astronaut type is not valid!")

    def add_planet(self, name, items):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."
        planet_obj = self.planet_factory.creating_a_planet_instance(name)
        items_list = items.split(', ')
        planet_obj.items.extend(items_list)
        self.planet_repository.add(planet_obj)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        astronauts_list = [x for x in self.astronaut_repository.astronauts if x.oxygen > 30]
        if not astronauts_list:
            raise Exception("You need at least one astronaut to explore the planet!")
        sorted_astros = sorted(astronauts_list, key=lambda x: -x.oxygen)
        astro_counter = 0
        for astro in sorted_astros[:5]:
            astro_counter += 1
            while planet.items:
                astro.backpack.append(planet.items.pop())
                astro.breathe()
                if astro.oxygen <= 0:
                    break
            else:
                self.missions_compleated += 1
                return f"Planet: {planet_name} was explored." \
                       f" {astro_counter} astronauts participated in collecting items."
        if planet.items:
            self.missions_not_compleated += 1
            return "Mission is not completed."

    def report(self):
        result = f"{self.missions_compleated} successful missions!\n"
        result += f"{self.missions_not_compleated} missions were not completed!\n"
        result += "Astronauts' info:\n"
        for astro in self.astronaut_repository.astronauts:
            result += f"Name: {astro.name}\n" \
                      f"Oxygen: {astro.oxygen}\n"
            if astro.backpack:
                result += f"Backpack items: {', '.join([x for x in astro.backpack])}\n"
            else:
                result += f'Backpack items: none\n'
        return result.strip()
