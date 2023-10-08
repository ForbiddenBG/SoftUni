from project.hardware.power_hardware import PowerHardware


class PowerHardwareFactory:

    @staticmethod
    def create_an_power_hardware_object(name, capacity, memory):
        return PowerHardware(name, capacity, memory)
