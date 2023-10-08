from project.core.user_factory import UserFactory


def find_user_by_username(name, my_list):
    for user in my_list:
        if name == user.username:
            return user


def find_movie_in_the_collection(movie, my_list):
    for el in my_list:
        if movie.title == el.title:
            return el


def unpack_and_setting_the_new_attributes(movie, kwargs):
    for attr, value in kwargs.items():
        if attr == "title":
            movie.title = value
        elif attr == 'year':
            movie.year = value
        elif attr == 'age_restriction':
            movie.age_restriction = value


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

        self.user_factory = UserFactory()

    def register_user(self, username, age):
        user = self.user_factory.creating_a_user(username, age)
        if find_user_by_username(username, self.users_collection):
            raise Exception("User already exists!")
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie):
        user = find_user_by_username(username, self.users_collection)
        if not user:
            raise Exception("This user does not exist!")
        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie, **kwargs):
        find_user_by_username(username, self.users_collection)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        unpack_and_setting_the_new_attributes(movie, kwargs)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie):
        user = find_user_by_username(username, self.users_collection)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie):
        user = find_user_by_username(username, self.users_collection)
        if not movie.owner.username == username and movie not in user.movies_liked:
            movie.likes += 1
            user.movies_liked.append(movie)
            return f"{username} liked {movie.title} movie."
        if movie.owner.username == username and movie not in user.movies_liked:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

    def dislike_movie(self, username, movie):
        user = find_user_by_username(username, self.users_collection)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = ""
        if sorted_movies:
            for j in sorted_movies:
                result += f"{j.details()}\n"
        else:
            return "No movies found."
        return result.strip()

    def __str__(self):
        result = ""
        if self.users_collection:
            result += f"All users: {', '.join([x.username for x in self.users_collection])}" + '\n'
        else:
            result += "All users: No users." + '\n'
        if self.movies_collection:
            result += f"All movies: {', '.join([x.title for x in self.movies_collection])}" + '\n'
        else:
            result += "All movies: No movies." + '\n'
        return result.strip()
