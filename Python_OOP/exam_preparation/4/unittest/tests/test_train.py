from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def test_correctly_initialized_constructor(self):
        train = Train("EXP", 10)
        self.assertEqual("EX", train.name)
        self.assertEqual(10, train.capacity)
        self.assertEqual([], train.passengers)

    def test_incorrect_adding_the_passenger_with_full_capacity_raises(self):
        train = Train("EXP", 2)
        train.passengers = ["Max", "Boris"]
        with self.assertRaises(ValueError) as context:
            train.add("Larry")
        self.assertEqual("Train is full", str(context.exception))

    def test_incorrect_adding_a_passenger_that_already_exists_raises(self):
        train = Train("EXP", 3)
        train.passengers = ["Max", "Boris"]
        with self.assertRaises(ValueError) as context:
            train.add("Max")
        self.assertEqual("Passenger Max Exists", str(context.exception))

    def test_correctly_adding_a_passenger(self):
        train = Train("EXP", 5)
        train.passengers = ["Max", "Boris"]
        result = train.add("Sonia")
        self.assertEqual("Added passenger Sonia", result)
        self.assertEqual(["Max", "Boris", "Sonia"], train.passengers)

    def test_incorrect_remove_of_passenger_that_doesnt_exist_raises(self):
        train = Train("EXP", 3)
        train.passengers = ["Max", "Boris"]
        with self.assertRaises(ValueError) as context:
            train.remove("Sonia")
        self.assertEqual("Passenger Not Found", str(context.exception))

    def test_correctly_remove_passenger(self):
        train = Train("EXP", 3)
        train.passengers = ["Max", "Boris"]
        result = train.remove("Boris")
        self.assertEqual("Removed Boris", result)
        self.assertEqual(["Max"], train.passengers)


if __name__ == "__main__":
    main()