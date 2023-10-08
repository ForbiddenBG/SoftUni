from project.planet.planet import Planet


class PlanetFactory:

    @staticmethod
    def creating_a_planet_instance(name):
        return Planet(name)
