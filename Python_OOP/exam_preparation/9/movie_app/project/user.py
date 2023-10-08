from project.core.validator import Validator


class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        Validator.if_the_string_is_empty(value, "Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.if_the_value_is_under_limit(value, 6, "Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        liked_movies = [movie.details() for movie in self.movies_liked]
        owned_movies = [movie.details() for movie in self.movies_owned]

        result = f"Username: {self.username}, Age: {self.age}\nLiked movies:\n"
        result += "No movies liked." if not self.movies_liked else '\n'.join(liked_movies)
        result += "\nOwned movies:\n"
        result += "No movies owned." if not self.movies_owned else '\n'.join(owned_movies)

        return result.strip()
