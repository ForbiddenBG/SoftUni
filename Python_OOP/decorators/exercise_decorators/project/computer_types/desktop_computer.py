from Python_OOP.decorators.exercise_decorators.project.computer_types.computer import Computer
from Python_OOP.decorators.exercise_decorators.project.core import available_components


class DesktopComputer(Computer):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        if processor not in available_components.desktop_available_processors:
            raise ValueError(f"{processor} is not compatible with desktop computer "
                             f"{self.manufacturer} {self.model}!")
        if ram not in available_components.desktop_available_rams:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer "
                             f"{self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        total_price = available_components.desktop_available_processors[processor] + available_components.desktop_available_rams[ram]
        self.price = total_price
        return f"Created {self.manufacturer} {self.model} with " \
               f"{self.processor} and {self.ram}GB RAM for {self.price}$."
