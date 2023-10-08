from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShopping(TestCase):
    def test_correctly_initialized_constructor(self):
        shop_cart = ShoppingCart("Metro", 100)
        self.assertEqual("Metro", shop_cart.shop_name)
        self.assertEqual(100, shop_cart.budget)
        self.assertEqual({}, shop_cart.products)

    def test_incorrect_name_with_first_small_letter_validation(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("metro", 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_incorrect_integers_instead_characters_validation(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("M37r0", 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_correctly_adding_the_product_to_the_cart(self):
        shop_cart = ShoppingCart("Metro", 100)
        result = shop_cart.add_to_cart("carrots", 20)
        self.assertEqual("carrots product was successfully added to the cart!", result)
        self.assertEqual({"carrots": 20}, shop_cart.products)

    def test_incorrect_adding_the_product_to_the_cart_with_price_more_or_equal_to_one_hundred_raises(self):
        shop_cart = ShoppingCart("Metro", 100)
        with self.assertRaises(ValueError) as ex:
            shop_cart.add_to_cart("carrots", 100)
        self.assertEqual("Product carrots cost too much!", str(ex.exception))

        shop_cart = ShoppingCart("Metro", 100)
        with self.assertRaises(ValueError) as ex:
            shop_cart.add_to_cart("carrots", 200)
        self.assertEqual("Product carrots cost too much!", str(ex.exception))

    def test_correctly_removing_the_product_from_the_products(self):
        shop_cart = ShoppingCart("Metro", 100)
        shop_cart.add_to_cart("banana", 10)
        shop_cart.add_to_cart("carrots", 20)
        self.assertEqual({"banana": 10, "carrots": 20}, shop_cart.products)
        result = shop_cart.remove_from_cart("banana")
        self.assertEqual("Product banana was successfully removed from the cart!", result)
        self.assertEqual({"carrots": 20}, shop_cart.products)

    def test_incorrect_removing_the_product_that_doesnt_exist(self):
        shop_cart = ShoppingCart("Metro", 100)
        shop_cart.add_to_cart("carrots", 10)
        with self.assertRaises(ValueError) as ex:
            shop_cart.remove_from_cart("banana")
        self.assertEqual("No product with name banana in the cart!", str(ex.exception))
        self.assertEqual({"carrots": 10}, shop_cart.products)

    def test_correctly_using_dunder_add_method(self):
        shop_cart = ShoppingCart("Metro", 50)
        shop_cart.products = {"banana": 20}
        shop_cart2 = ShoppingCart("Bio", 50)
        shop_cart2.products = {"carrots": 20, "ketchup": 10}
        new_shop = shop_cart.__add__(shop_cart2)
        self.assertEqual("MetroBio", new_shop.shop_name)
        self.assertEqual(100, new_shop.budget)
        self.assertEqual({"banana": 20, "carrots": 20, "ketchup": 10}, new_shop.products)

    def test_correctly_buying_products(self):
        shop_cart = ShoppingCart("Metro", 50)
        shop_cart.add_to_cart("banana", 20)
        shop_cart.add_to_cart("carrots", 10)
        result = shop_cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 30.00lv.', result)

    def test_incorrect_buying_products_with_total_price_over_budget(self):
        shop_cart = ShoppingCart("Metro", 50)
        shop_cart.add_to_cart("banana", 40)
        shop_cart.add_to_cart("carrots", 20)
        with self.assertRaises(ValueError) as ex:
            shop_cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 10.00lv!", str(ex.exception))


if __name__ == "__main__":
    main()
