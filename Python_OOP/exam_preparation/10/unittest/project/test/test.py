from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):
    def test_correctly_initiated_constructor(self):
        movie = Movie("Gladiator", 2004, 9.4)
        self.assertEqual("Gladiator", movie.name)
        self.assertEqual(2004, movie.year)
        self.assertEqual(9.4, movie.rating)
        self.assertEqual([], movie.actors)

    def test_correctly_setting_the_name_validation(self):
        movie = Movie("Titanic", 1994, 8)
        movie.name = "Titanic"
        self.assertEqual("Titanic", movie.name)

    def test_incorrectly_setting_the_name_validation_with_empty_string_raises(self):
        movie = Movie("Titanic", 1994, 8)
        with self.assertRaises(ValueError) as context:
            movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(context.exception))

    def test_correctly_setting_the_year_validation(self):
        movie = Movie("Species", 1994, 7)
        movie.year = 1994
        self.assertEqual(1994, movie.year)

    def test_incorrectly_setting_the_year_under_1887_raises(self):
        movie = Movie("Species", 1994, 7)
        with self.assertRaises(ValueError) as context:
            movie.year = 1880
        self.assertEqual("Year is not valid!", str(context.exception))

    def test_adding_an_actor_correctly(self):
        movie = Movie("Mad Max", 1994, 10)
        movie.actors = []
        movie.add_actor("Mel Gibson")
        self.assertEqual(["Mel Gibson"], movie.actors)

    def test_adding_an_exsiting_actor(self):
        movie = Movie("Mad Max", 1994, 10)
        movie.actors = ["Mel Gibson"]
        result = movie.add_actor("Mel Gibson")
        self.assertEqual("Mel Gibson is already added in the list of actors!", result)

    def test_the_rating_is_greater_than_the_other_movie_correct(self):
        movie1 = Movie("Mad Max", 1994, 10)
        movie2 = Movie("Screamers", 1994, 9)
        result = movie1.__gt__(movie2)
        self.assertEqual('"Mad Max" is better than "Screamers"', result)

    def test_the_rating_is_lesser_than_the_other_movie_correct(self):
        movie1 = Movie("Mad Max", 1994, 9)
        movie2 = Movie("Screamers", 1994, 10)
        result = movie1.__gt__(movie2)
        self.assertEqual('"Screamers" is better than "Mad Max"', result)

    def test_the_movies_have_equal_rating(self):
        movie1 = Movie("Mad Max", 1994, 10)
        movie2 = Movie("Screamers", 1994, 10)
        result = movie1.__gt__(movie2)
        self.assertEqual('"Screamers" is better than "Mad Max"', result)

    def test_valid_dunder_repr(self):
        movie = Movie("Alien", 1994, 10)
        movie.actors = ["Henry", "Sigourney"]
        result = movie.__repr__()
        self.assertEqual("Name: Alien\n"
                         "Year of Release: 1994\n"
                         "Rating: 10.00\n"
                         "Cast: Henry, Sigourney", result)


if __name__ == "__main__":
    main()
