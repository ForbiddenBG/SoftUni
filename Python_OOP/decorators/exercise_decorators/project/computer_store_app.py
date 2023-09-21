from Python_OOP.decorators.exercise_decorators.project.computer_types.desktop_computer import DesktopComputer
from Python_OOP.decorators.exercise_decorators.project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
            result = computer.configure_computer(processor, ram)
            self.warehouse.append(computer)
            return result
        if type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
            result = computer.configure_computer(processor, ram)
            self.warehouse.append(computer)
            return result
        raise ValueError(f"{ type_computer } is not a valid type computer!")

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for pc in self.warehouse:
            if client_budget >= pc.price and wanted_processor == pc.processor and wanted_ram <= pc.ram:
                self.profits += client_budget - pc.price
                self.warehouse.remove(pc)
                return f"{ repr(pc) } sold for { client_budget }$."
        raise Exception("Sorry, we don't have a computer for you.")
