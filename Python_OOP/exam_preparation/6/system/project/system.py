from project.core.express_software_factory import ExpressSoftwareFactory
from project.core.heavy_hardware_factory import HeavyHardwareFactory
from project.core.light_software_factory import LightSoftwareFactory
from project.core.power_hardware_factory import PowerHardwareFactory


def find_entity_by_name(name, my_list):
    for entity in my_list:
        if name == entity.name:
            return entity


class System:
    _hardware = []
    _software = []

    power_hardware_factory = PowerHardwareFactory()
    heavy_hardware_factory = HeavyHardwareFactory()
    express_software_factory = ExpressSoftwareFactory()
    light_software_factory = LightSoftwareFactory()

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = System.power_hardware_factory.create_an_power_hardware_object(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = System.heavy_hardware_factory.create_a_heavy_hardware_object(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = find_entity_by_name(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"
        express_software = System.express_software_factory.create_an_express_software_object(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = find_entity_by_name(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"
        light_software = System.light_software_factory.create_a_light_software_object(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = find_entity_by_name(hardware_name, System._hardware)
        software = find_entity_by_name(software_name, System._software)
        if hardware and software:
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: " \
                  f"{sum([x.memory_consumption for x in System._software])} / {sum([x.memory for x in System._hardware])}\n"
        result += f"Total Capacity Taken: " \
                  f"{sum([x.capacity_consumption for x in System._software])} / {sum([x.capacity for x in System._hardware])}\n"
        return result.strip()

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            result += f"Express Software Components:" \
                      f" {len([x for x in hardware.software_components if x.software_type == 'Express'])}\n"
            result += f"Light Software Components:" \
                      f" {len([x for x in hardware.software_components if x.software_type == 'Light'])}\n"
            result += f"Memory Usage: " \
                      f"{sum([x.memory_consumption for x in hardware.software_components])} / {hardware.memory}\n"
            result += f"Capacity Usage: " \
                      f"{sum([x.capacity_consumption for x in hardware.software_components])} / {hardware.capacity}\n"
            result += f"Type: {hardware.hardware_type}\n"
            result += f"Software Components: " \
                      f"{', '.join([x.name if hardware.software_components else 'None' for x in hardware.software_components])}\n"
        return result.strip()
