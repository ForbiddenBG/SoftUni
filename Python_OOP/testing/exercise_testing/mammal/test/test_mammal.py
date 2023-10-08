from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def test_correctly_initialized_init(self):
        mammal = Mammal("Tom", "cat", "prr")
        self.assertEqual("Tom", mammal.name)
        self.assertEqual("cat", mammal.type)
        self.assertEqual("prr", mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_correctly_makes_a_sound(self):
        mammal = Mammal("Tom", "cat", "prr")
        expected = mammal.make_sound()
        self.assertEqual("Tom makes prr", expected)

    def test_return_correct_kingdom(self):
        mammal = Mammal("Tom", "cat", "prr")
        expected = mammal.get_kingdom()
        self.assertEqual("animals", expected)

    def test_correctly_get_info(self):
        mammal = Mammal("Tom", "cat", "prr")
        expected = mammal.info()
        result = "Tom is of type cat"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()


# from unittest import TestCase, main
#
#
# # local import path
# from testing_exercise.mammal.project.mammal import Mammal
#
# # import for Judge
# #from project.mammal import Mammal
#
#
# class MammalTests(TestCase):
#     # we use setUp to use the instance Mammal for all other test and avoid a repetition of  the same code
#     # -> None - defining a functions that returns None it can work without -> None as well
#     def setUp(self) -> None:
#         self.mammal = Mammal("name", "mammal_type", "sound")
#
#     # testing the __init__
#     def test_mammal_init(self):
#         name = "Peter"
#         mammal_type = "Mammal Type"
#         sound = "sound"
#         mammal = Mammal(name, mammal_type, sound)
#
#         self.assertEqual(mammal.name, name)
#         self.assertEqual(mammal.type, mammal_type)
#         self.assertEqual(mammal.sound, sound)
#         # checking if the private attribute works
#         self.assertEqual(mammal._Mammal__kingdom, "animals")
#
#     # testing make_sound
#     def test_make_sound_returns_proper_string(self):
#         expected_result = f"{self.mammal.name} makes {self.mammal.sound}"
#         actual_result = self.mammal.make_sound()
#
#         self.assertEqual(expected_result, actual_result)
#
#     # test get_kingdom method - the method will return a constant animals,
#     # returns the private attribute self.__kingdom which is equal to "animals"
#     def test_get_kingdom_returns_animals(self):
#         self.assertEqual(self.mammal.get_kingdom(), self.mammal._Mammal__kingdom)
#
#     # test method info
#     def test_info_returns_proper_string(self):
#         expected_result = f"{self.mammal.name} is of type {self.mammal.type}"
#         actual_result = self.mammal.info()
#
#         self.assertEqual(expected_result, actual_result)
#
#
# if __name__ == "__main__":
#     main()
