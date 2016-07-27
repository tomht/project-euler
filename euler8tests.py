import euler8
import unittest


class LargestProductInNumberStringTestCase(unittest.TestCase):
    def test_largest_2_digit_product_in_12345678987654321_is_72(self):
        self.assertEquals(72, euler8.largest_product_in_number_string("12345678987654321", 2))

    def test_largest_3_digit_product_in_1023045607809_is_120(self):
        self.assertEquals(120, euler8.largest_product_in_number_string("1023045607809", 3))


class Euler8TestCase(unittest.TestCase):
    def test_euler8_returns_23514624000(self):
        self.assertEquals(23514624000, euler8.euler8())
