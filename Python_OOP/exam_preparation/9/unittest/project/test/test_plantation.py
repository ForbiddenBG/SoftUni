from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def test_initialized_correctly_constructor(self):
        plantation = Plantation(10)
        self.assertEqual(10, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_validation_correctly_set(self):
        plantation = Plantation(10)
        plantation.size = 10
        self.assertEqual(10, plantation.size)

    def test_validation_incorrectly_set_raises(self):
        plantation = Plantation(10)
        with self.assertRaises(ValueError) as context:
            plantation.size = -1
        self.assertEqual("Size must be positive number!", str(context.exception))

    def test_correctly_hire_worker(self):
        plantation = Plantation(10)
        plantation.workers = []
        result = plantation.hire_worker("Alex")
        self.assertEqual(["Alex"], plantation.workers)
        self.assertEqual("Alex successfully hired.", result)

    def test_incorrectly_hire_worker_raises(self):
        plantation = Plantation(10)
        plantation.workers = ["Alex"]
        with self.assertRaises(ValueError) as context:
            plantation.hire_worker("Alex")
        self.assertEqual("Worker already hired!", str(context.exception))

    def test_dunder_len(self):
        plantation = Plantation(10)
        plantation.plants = {"Alex": ["tulip"]}
        result = plantation.__len__()
        self.assertEqual(1, result)

    def test_planting_with_missing_worker_raises(self):
        plantation = Plantation(10)
        plantation.workers = []
        with self.assertRaises(ValueError) as context:
            plantation.planting("Alex", "tulip")
        self.assertEqual("Worker with name Alex is not hired!", str(context.exception))

    def test_planting_with_full_capacity_plants_over_the_capacity_raises(self):
        plantation = Plantation(2)
        plantation.plants = {"Max": ["tulip"], "Boris": ["palm"]}
        plantation.workers = ["Alex"]
        with self.assertRaises(ValueError) as context:
            plantation.planting("Alex", "orchid")
        self.assertEqual("The plantation is full!", str(context.exception))

    def test_planting_with_full_capacity_plants_equal_to_zero_raises(self):
        plantation = Plantation(1)
        plantation.plants = {"Max": ["tulip"]}
        plantation.workers = ["Alex"]
        with self.assertRaises(ValueError) as context:
            plantation.planting("Alex", "orchid")
        self.assertEqual("The plantation is full!", str(context.exception))

    def test_planting_correctly_with_worker_as_a_key_appending_new_flower(self):
        plantation = Plantation(10)
        plantation.plants = {"Alex": ["tulip"]}
        plantation.workers = ["Alex"]
        result = plantation.planting("Alex", "daffodil")
        self.assertEqual({"Alex": ["tulip", "daffodil"]}, plantation.plants)
        self.assertEqual("Alex planted daffodil.", result)

    def test_planting_correctly_with_worker_as_a_key_and_new_list_as_a_value(self):
        plantation = Plantation(10)
        plantation.plants = {}
        plantation.workers = ["Alex"]
        result = plantation.planting("Alex", "daffodil")
        self.assertEqual({"Alex": ["daffodil"]}, plantation.plants)
        self.assertEqual("Alex planted it's first daffodil.", result)

    def test_correctly_representing_the_dunder_str(self):
        plantation = Plantation(10)
        plantation.plants = {"Max": ["tulip", "palm"]}
        plantation.workers = ["Max", "Alex"]
        result = plantation.__str__()
        self.assertEqual("Plantation size: 10\n"
                         "Max, Alex\n"
                         "Max planted: tulip, palm", result)

    def test_correctly_representing_the_dunder_repr(self):
        plantation = Plantation(10)
        plantation.plants = {"Max": ["tulip", "palm"]}
        plantation.workers = ["Max", "Alex", "Boris", "Larry"]
        result = plantation.__repr__()
        self.assertEqual('Size: 10\n'
                         'Workers: Max, Alex, Boris, Larry', result)


if __name__ == "__main__":
    main()