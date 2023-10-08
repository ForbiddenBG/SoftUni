from project.jockey import Jockey


class JockeyFactory:

    @staticmethod
    def creating_a_jockey(jockey_name, age):
        return Jockey(jockey_name, age)
