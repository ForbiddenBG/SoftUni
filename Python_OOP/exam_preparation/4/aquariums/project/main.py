from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.controller import Controller
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

controller = Controller()
fish1 = FreshwaterFish("Max", "shark", 10)
fish2 = SaltwaterFish("Jack", "horse", 15)
aquarium1 = SaltwaterAquarium("Alabala")
aquarium2 = FreshwaterAquarium("Blabla")

print(controller.add_aquarium("FreshwaterAquarium", "Blabla"))
print(controller.add_fish("Blabla", "FreshwaterFish", "Max", "horse", 15))
# print(controller.add_fish("Alabala", "FreshwaterFish", "Max", "shark", 10))