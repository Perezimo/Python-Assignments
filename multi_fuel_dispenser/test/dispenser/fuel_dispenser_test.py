import unittest

from src.dispenser.fuel_dispenser import Dispenser


class FuelTestCase(unittest.TestCase):
    def setUp(self):
        self.dispenser = Dispenser()
        self.dispenser.reset_quantity()


    def test_that_i_can_buy_fuel(self):
        self.assertEqual(300, self.dispenser.check_quantity("Petrol"))
        self.dispenser.buy_fuel_with_liter("Petrol", 10)
        self.assertEqual(290, self.dispenser.check_quantity("Petrol"))

    def test_that_i_can_buy_fuel_with_quantity(self):
        self.assertEqual(300, self.dispenser.check_quantity("Petrol"))
        self.dispenser.buy_fuel_with_liter("Petrol", 50)
        self.assertEqual(250, self.dispenser.check_quantity("Petrol"))

    def test_that_i_can_not_buy_fuel_more_than_50L(self):
        self.assertEqual(300, self.dispenser.check_quantity("Petrol"))
        self.dispenser.buy_fuel_with_liter("Petrol", 60)
        self.assertEqual(300, self.dispenser.check_quantity("Petrol"))

    def test_that_i_can_not_buy_fuel_less_than_1L(self):
        self.assertEqual(300, self.dispenser.check_quantity("Petrol"))
        self.dispenser.buy_fuel_with_liter("Petrol", 0.4)
        self.assertEqual(300, self.dispenser.check_quantity("Petrol"))

    def test_that_i_can_buy_fuel_by_amount(self):
        self.assertEqual(300, self.dispenser.check_quantity("Petrol"))
        self.dispenser.buy_fuel_with_amount("Petrol", 2600)
        self.assertEqual(298, self.dispenser.check_quantity("Petrol"))


if __name__ == '__main__':
    unittest.main()
