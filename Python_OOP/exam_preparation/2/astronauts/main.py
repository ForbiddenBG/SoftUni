from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.space_station import SpaceStation

space_station = SpaceStation()
astro1 = Biologist("Max")
astro2 = Geodesist("Alex")
astro3 = Geodesist("Peter")
astro4 = Meteorologist("Sonia")
astro5 = Biologist("Bucks")
astro6 = Biologist("Snoopy")
astro7 = Meteorologist("Brain")

planet1 = Planet("Mars")
planet2 = Planet("Saturn")

planet_rep = PlanetRepository()
astro_rep = AstronautRepository()


space_station.add_astronaut("Biologist", "Max")
space_station.add_astronaut("Geodesist", "Alex")
space_station.add_astronaut("Geodesist", "Peter")
space_station.add_astronaut("Meteorologist", "Sonia")
space_station.add_astronaut("Biologist", "Bucks")
space_station.add_astronaut("Biologist", "Snoopy")
space_station.add_astronaut("Biologist", "Brain")

items = "rock, selenium, diamond, iron, copper, plasma, shards"
print(space_station.add_planet("Mars", items))

print(space_station.send_on_mission("Mars"))
print(space_station.report())
