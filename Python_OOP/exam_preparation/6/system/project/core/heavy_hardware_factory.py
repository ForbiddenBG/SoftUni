from project.hardware.heavy_hardware import HeavyHardware


class HeavyHardwareFactory:

    @staticmethod
    def create_a_heavy_hardware_object(name, capacity, memory):
        return HeavyHardware(name, capacity, memory)
