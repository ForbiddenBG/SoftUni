from unittest import TestCase, main
from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def test_correctly_initialized_constructor(self):
        pets = PetShop("Animals")
        self.assertEqual("Animals", pets.name)
        self.assertEqual({}, pets.food)
        self.assertEqual([], pets.pets)

    def test_incorrectly_adding_food_with_zero_value_raise(self):
        pets = PetShop("Animals")
        with self.assertRaises(ValueError) as context:
            pets.add_food("meat", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_incorrectly_adding_food_with_value_below_zero_raise(self):
        pets = PetShop("Animals")
        with self.assertRaises(ValueError) as context:
            pets.add_food("meat", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_correctly_adding_food_to_the_dictionary(self):
        pets = PetShop("Animals")
        result = pets.add_food("meat", 10)
        self.assertEqual({"meat": 10}, pets.food)
        self.assertEqual("Successfully added 10.00 grams of meat.", result)

    def test_correctly_adding_a_pet_to_the_shop(self):
        petz = PetShop("Animals")
        result = petz.add_pet("Max")
        self.assertEqual(["Max"], petz.pets)
        self.assertEqual("Successfully added Max.", result)

    def test_incorrectly_adding_a_pet_to_the_shop_raise(self):
        petz = PetShop("Animals")
        petz.pets = ["Max"]
        with self.assertRaises(Exception) as context:
            petz.add_pet("Max")
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_incorrectly_feed_the_pet_raise(self):
        petz = PetShop("Animals")
        petz.pets = ["Max"]
        with self.assertRaises(Exception) as context:
            petz.feed_pet("bread", "Zorro")
        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test_incorrectly_feed_the_pet_with_food_that_doesnt_exist(self):
        petz = PetShop("Animals")
        petz.pets = ["Max"]
        petz.food = {"meat": 10}
        result = petz.feed_pet("bread", "Max")
        self.assertEqual('You do not have bread', result)

    def test_incorrectly_feed_the_pet_with_amount_of_food_under_100(self):
        petz = PetShop("Animals")
        petz.pets = ["Max"]
        petz.food = {"meat": 10}
        result = petz.feed_pet("meat", "Max")
        self.assertEqual({"meat": 1010}, petz.food)
        self.assertEqual("Adding food...", result)

    def test_correctly_feed_the_pet(self):
        petz = PetShop("Animals")
        petz.pets = ["Max"]
        petz.food = {"meat": 200}
        result = petz.feed_pet("meat", "Max")
        self.assertEqual({"meat": 100}, petz.food)
        self.assertEqual("Max was successfully fed", result)

    def test_valid_repr_method(self):
        petz = PetShop("Animals")
        petz.pets = ["Max", "Zorro"]
        result = petz.__repr__()
        self.assertEqual('Shop Animals:\n'
                         'Pets: Max, Zorro', result)


if __name__ == "__main__":
    main()
