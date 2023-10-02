from project.core.Validator import Validator


class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.if_name_contains_empty_string_or_white_spaces(value, "Name cannot be an empty string!")
        self.__name = value
