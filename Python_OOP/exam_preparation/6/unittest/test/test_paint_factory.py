from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def test_correctly_initiated_constructor(self):
        factory = PaintFactory("Zero", 10)
        self.assertEqual("Zero", factory.name)
        self.assertEqual(10, factory.capacity)
        self.assertEqual({}, factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], factory.valid_ingredients)

    def test_add_ingredients_correctly_with_quantity_less_than_twenty(self):
        factory = PaintFactory("Zero", 20)
        factory.ingredients = {}
        factory.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        factory.add_ingredient("white", 5)
        self.assertEqual({"white": 5}, factory.ingredients)

    def test_add_ingredients_correctly_with_quantity_equal_to_zero(self):
        factory = PaintFactory("Zero", 20)
        factory.ingredients = {}
        factory.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        factory.add_ingredient("yellow", 0)
        self.assertEqual({"yellow": 0}, factory.ingredients)

    def test_add_ingredients_incorrectly_with_value_above_the_edge_case_raises(self):
        factory = PaintFactory("Zero", 20)
        factory.ingredients = {}
        factory.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        with self.assertRaises(ValueError) as context:
            factory.add_ingredient("white", 25)
        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_add_ingredients_incorrectly_with_wrong_type_of_ingredient_raises(self):
        factory = PaintFactory("Zero", 20)
        factory.ingredients = {}
        factory.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        with self.assertRaises(TypeError) as context:
            factory.add_ingredient("black", 4)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(context.exception))

    def test_remove_ingredients_correctly_with_less_quantity(self):
        factory = PaintFactory("Zero", 20)
        factory.ingredients = {"yellow": 10}
        factory.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        factory.remove_ingredient("yellow", 5)
        self.assertEqual({"yellow": 5}, factory.ingredients)

    def test_remove_ingredients_correctly_with_the_same_quantity(self):
        factory = PaintFactory("Zero", 20)
        factory.ingredients = {"yellow": 10}
        factory.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        factory.remove_ingredient("yellow", 10)
        self.assertEqual({"yellow": 0}, factory.ingredients)

    def test_invalid_remove_ingredients_with_less_quantity_than_zero_raises(self):
        factory = PaintFactory("Zero", 20)
        factory.ingredients = {"yellow": 10}
        factory.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        with self.assertRaises(ValueError) as context:
            factory.remove_ingredient("yellow", 20)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_invalid_remove_ingredients_that_doesnt_exist_raises(self):
        factory = PaintFactory("Zero", 20)
        factory.ingredients = {"yellow": 10}
        factory.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        with self.assertRaises(KeyError) as context:
            factory.remove_ingredient("black", 10)
        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_correctly_return_products(self):
        factory = PaintFactory("Zero", 20)
        factory.ingredients = {"yellow": 10}
        self.assertEqual({"yellow": 10}, factory.products)

    def test_returning_valid_repr_dunder(self):
        factory = PaintFactory("Zero", 30)
        factory.ingredients = {"yellow": 10, "white": 10}
        result = factory.__repr__()
        self.assertEqual("Factory name: Zero with capacity 30.\n"
                         "yellow: 10\n"
                         "white: 10\n", result)

if __name__ == "__main__":
    main()