from project.driver import Driver


class DriverFactory:

    @staticmethod
    def creating_a_driver_instance(name):
        return Driver(name)
