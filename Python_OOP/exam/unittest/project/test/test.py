from project.movie import Movie
from unittest import TestCase, main

class TestMovie(TestCase):
    def test_initiation(self):
        movie = Movie("One", 2000, 10)
        self.assertEqual("One", movie.name)
        self.assertEqual(2000, movie.year)
        self.assertEqual(10, movie.rating)
        self.assertEqual([], movie.actors)

    def test_if_name_is_empty_string(self):
        with self.assertRaises(Exception) as ex:
            movie = Movie("", 2000, 10)
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_if_year_is_less_than_1887(self):
        with self.assertRaises(Exception) as ex:
            movie = Movie("One", 1800, 10)
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_if_actor_not_in_actors(self):
        movie = Movie("One", 2000, 10)
        movie.actors = []
        movie.add_actor("Henry")
        self.assertEqual(["Henry"], movie.actors)

    def test_if_actor_in_actors(self):
        movie = Movie("One", 2000, 10)
        movie.actors = ["Henry"]
        res = movie.add_actor("Henry")
        self.assertEqual("Henry is already added in the list of actors!", res)

    def test_is_rating_is_greather(self):
        movie1 = Movie("One", 2000, 10)
        movie2 = Movie("Two", 2000, 9)
        res = movie1>movie2
        self.assertEqual('"One" is better than "Two"', res)

    def test_is_rating_less(self):
        movie1 = Movie("One", 2000, 9)
        movie2 = Movie("Two", 2000, 10)
        res = movie1 < movie2
        self.assertEqual('"Two" is better than "One"', res)

    def test_are_equal(self):
        movie1 = Movie("One", 2000, 10)
        movie2 = Movie("Two", 2000, 10)
        res = movie1 > movie2
        self.assertEqual('"Two" is better than "One"', res)

    def test_report(self):
        movie = Movie("One", 2000, 10)
        movie.actors = ["Harry", "Benny"]
        expected = "Name: One\n" \
               "Year of Release: 2000\n" \
               "Rating: 10.00\n" \
               "Cast: Harry, Benny"
        self.assertEqual(expected, movie.__repr__())

if __name__ == '__main__':
    main()