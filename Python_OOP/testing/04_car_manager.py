
# class Car:
#     def __init__(self, make, model, fuel_consumption, fuel_capacity):
#         self.make = make
#         self.model = model
#         self.fuel_consumption = fuel_consumption
#         self.fuel_capacity = fuel_capacity
#         self.fuel_amount = 0
#
#     @property
#     def make(self):
#         return self.__make
#
#     @make.setter
#     def make(self, new_value):
#         if not new_value:
#             raise Exception("Make cannot be null or empty!")
#         self.__make = new_value
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, new_value):
#         if not new_value:
#             raise Exception("Model cannot be null or empty!")
#         self.__model = new_value
#
#     @property
#     def fuel_consumption(self):
#         return self.__fuel_consumption
#
#     @fuel_consumption.setter
#     def fuel_consumption(self, new_value):
#         if new_value <= 0:
#             raise Exception("Fuel consumption cannot be zero or negative!")
#         self.__fuel_consumption = new_value
#
#     @property
#     def fuel_capacity(self):
#         return self.__fuel_capacity
#
#     @fuel_capacity.setter
#     def fuel_capacity(self, new_value):
#         if new_value <= 0:
#             raise Exception("Fuel capacity cannot be zero or negative!")
#         self.__fuel_capacity = new_value
#
#     @property
#     def fuel_amount(self):
#         return self.__fuel_amount
#
#     @fuel_amount.setter
#     def fuel_amount(self, new_value):
#         if new_value < 0:
#             raise Exception("Fuel amount cannot be negative!")
#         self.__fuel_amount = new_value
#
#     def refuel(self, fuel):
#         if fuel <= 0:
#             raise Exception("Fuel amount cannot be zero or negative!")
#         self.__fuel_amount += fuel
#         if self.__fuel_amount > self.__fuel_capacity:
#             self.__fuel_amount = self.__fuel_capacity
#
#     def drive(self, distance):
#         needed = (distance / 100) * self.__fuel_consumption
#
#         if needed > self.__fuel_amount:
#             raise Exception("You don't have enough fuel to drive!")
#
#         self.__fuel_amount -= needed


from unittest import TestCase, main

from project.main import Car


class CarTest(TestCase):
    def test_initialized_the_constructor_correctly(self):
        car = Car("a", "Opel", 10, 100)
        self.assertEqual("a", car.make)
        self.assertEqual("Opel", car.model)
        self.assertEqual(10, car.fuel_consumption)
        self.assertEqual(100, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_validation_make_with_correct_data(self):
        car = Car("a", "Opel", 10, 100)
        car.make = "b"
        self.assertEqual("b", car.make)

    def test_validation_make_with_incorrect_data_raises(self):
        car = Car("a", "Opel", 10, 100)
        with self.assertRaises(Exception) as ex:
            car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_validation_make_with_null_raises(self):
        car = Car("a", "Opel", 10, 100)
        with self.assertRaises(Exception) as ex:
            car.make = None
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_validation_model_with_correct_data(self):
        car = Car("a", "Opel", 10, 100)
        car.model = "Lada"
        self.assertEqual("Lada", car.model)

    def test_validation_model_incorrect_raises(self):
        car = Car("a", "Opel", 10, 100)
        with self.assertRaises(Exception) as ex:
            car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_validation_model_with_null_raises(self):
        car = Car("a", "Opel", 10, 100)
        with self.assertRaises(Exception) as ex:
            car.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_valid_fuel_consumption(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_consumption = 20
        self.assertEqual(20, car.fuel_consumption)

    def test_invalid_fuel_consumption_with_zero_raises(self):
        car = Car("a", "Opel", 10, 100)
        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_invalid_fuel_consumption_with_negative_raises(self):
        car = Car("a", "Opel", 10, 100)
        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_valid_fuel_capacity(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_capacity = 200
        self.assertEqual(200, car.fuel_capacity)

    def test_fuel_capacity_with_zero_raises(self):
        car = Car("a", "Opel", 10, 100)
        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_raises(self):
        car = Car("a", "Opel", 10, 100)
        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_correct(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_amount = 10
        self.assertEqual(10, car.fuel_amount)

    def test_fuel_amount_with_zero(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_amount = 0
        self.assertEqual(0, car.fuel_amount)

    def test_fuel_amount_with_negative_raises(self):
        car = Car("a", "Opel", 10, 100)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_correct(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_amount = 0
        car.refuel(9)
        self.assertEqual(9, car.fuel_amount)

    def test_refuel_with_more_than_the_capacity_allows(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_amount = 0
        car.refuel(200)
        self.assertEqual(100, car.fuel_amount)

    def test_refuel_with_zero_raises(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_amount = 0
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_negative_raises(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_amount = 0
        with self.assertRaises(Exception) as ex:
            car.refuel(-15)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_with_correct(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_amount = 50
        car.drive(400)
        self.assertEqual(10, car.fuel_amount)

    def test_drive_with_equal_consumption(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_amount = 50
        car.drive(500)
        self.assertEqual(0, car.fuel_amount)

    def test_drive_with_over_consumption_raises(self):
        car = Car("a", "Opel", 10, 100)
        car.fuel_amount = 50
        with self.assertRaises(Exception) as ex:
            car.drive(700)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()