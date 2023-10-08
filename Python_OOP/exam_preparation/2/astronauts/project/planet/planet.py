from project.core.validator import Validator


class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.is_empty_string_or_white_spaces(value, "Planet name cannot be empty string or whitespace!")
        self.__name = value
