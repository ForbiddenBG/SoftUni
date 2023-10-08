from abc import ABC, abstractmethod
from project.core.validator import Validator
from project.user import User


class Movie(ABC):
    @abstractmethod
    def __init__(self, title, year, owner, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        Validator.if_the_string_is_empty(value, "The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        Validator.if_the_movie_was_released_under_the_year_1888(value, "Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        Validator.if_the_atribute_is_not_an_object(value, User, "The owner must be an object of type User!")
        self.__owner = value

    @abstractmethod
    def details(self):
        pass
