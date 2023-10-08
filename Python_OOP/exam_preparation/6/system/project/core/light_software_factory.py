from project.software.light_software import LightSoftware


class LightSoftwareFactory:

    @staticmethod
    def create_a_light_software_object(name, capacity_consumption, memory_consumption):
        return LightSoftware(name, capacity_consumption, memory_consumption)
