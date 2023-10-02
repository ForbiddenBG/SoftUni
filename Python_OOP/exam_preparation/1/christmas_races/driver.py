from project.core.Validator import Validator


class Driver:
    def __init__(self, name):
        self.name = name
        self.car = None
        # One driver drives only one car!
        self.number_of_wins = 0
        # If the driver wins the race the number of wins should increase!

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.if_name_contains_empty_string_or_white_spaces(value, "Name should contain at least one character!")
        self.__name = value
