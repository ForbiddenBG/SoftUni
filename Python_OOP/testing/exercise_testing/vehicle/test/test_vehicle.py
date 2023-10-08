from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def test_setting_the_right_class_atributes_and_init(self):
        vehicle = Vehicle(100.0, 20.0)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(100.0, vehicle.fuel)
        self.assertEqual(100.0, vehicle.capacity)
        self.assertEqual(20.0, vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)

    def test_drive_with_correct_parameters(self):
        vehicle = Vehicle(100.0, 20.0)
        vehicle.drive(10)
        self.assertEqual(87.5, vehicle.fuel)

    def test_drive_with_incorrect_parameters(self):
        vehicle = Vehicle(10.0, 20.0)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_correct_parameters(self):
        vehicle = Vehicle(100.0, 20.0)
        vehicle.drive(10)
        vehicle.refuel(10)
        self.assertEqual(97.5, vehicle.fuel)

    def test_refuel_with_more_than_the_capacity(self):
        vehicle = Vehicle(100.0, 20.0)
        vehicle.drive(10)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_correctly_returning_the_value_of_the_dunder_str(self):
        vehicle = Vehicle(100.0, 20.0)
        result = f"The vehicle has 20.0 " \
                 f"horse power with 100.0 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, vehicle.__str__())


if __name__ == "__main__":
    main()
