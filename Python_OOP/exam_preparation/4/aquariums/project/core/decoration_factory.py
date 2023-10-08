from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationFactory:
    valid_types = {"Ornament": Ornament, "Plant": Plant}

    @staticmethod
    def create_a_decoration_object(decoration_type):
        return DecorationFactory.valid_types[decoration_type]()
