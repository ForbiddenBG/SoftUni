from project.software.express_software import ExpressSoftware


class ExpressSoftwareFactory:

    @staticmethod
    def create_an_express_software_object(name, capacity_consumption, memory_consumption):
        return ExpressSoftware(name, capacity_consumption, memory_consumption)
