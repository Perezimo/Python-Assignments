import unittest

from main import product
from src.checkout.checkout import Checkout


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.check_out = Checkout()
        self.check_out.remove_products()

    def test_that_product_can_be_added(self):
        self.check_out.add_product('apple', 5000, 5)
        self.assertEqual(1, self.check_out.check_cart_quantity())

    def test_that_product_quantity_can_be_added(self):
        self.check_out.add_product('apple', 5000, 5)
        self.check_out.add_product('orange', 7000, 4)
        self.assertEqual(5, self.check_out.check_cart_product_quantity("apple"))

    def test_that_product_price_can_be_added(self):
        self.check_out.add_product('apple', 5000, 5)
        self.check_out.add_product('orange', 7000, 4)
        self.assertEqual(5000, self.check_out.check_product_price("apple"))

    def test_that_more_than_a_product_can_be_added(self):
        self.check_out.add_product('apple', 5000, 5)
        self.check_out.add_product('orange', 7000, 4)
        self.assertEqual(2, self.check_out.check_cart_quantity())

    def test_that_total_price_can_be_calculated(self):
        self.check_out.add_product('apple', 5000, 5)
        self.check_out.add_product('orange', 7000, 4)
        self.assertEqual(53000, self.check_out.calculate_sub_total())

    def test_that_total_price_for_each_product_can_be_calculated(self):
        self.check_out.add_product('apple', 5000, 5)
        self.check_out.add_product('orange', 7000, 4)
        self.assertEqual(25000, self.check_out.calculate_total_per_product("apple"))

    def test_that_total_price_can_be_calculated_after_discount(self):
        self.check_out.add_product('apple', 5000, 5)
        self.check_out.add_product('orange', 7000, 4)
        self.assertEqual(3710, self.check_out.calculate_discount(7))

    def test_vat_can_be_calculated_on_total_price(self):
        self.check_out.add_product('apple', 5000, 5)
        self.check_out.add_product('orange', 7000, 4)
        self.assertEqual(3975, self.check_out.calculate_vat())

    def test_that_total_price_can_be_calculated_after_discount_and_vat(self):
        self.check_out.add_product('apple', 5000, 5)
        self.check_out.add_product('orange', 7000, 4)
        self.assertEqual(53265, self.check_out.calculate_total(7))


if __name__ == '__main__':
    unittest.main()
