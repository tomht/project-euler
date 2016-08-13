import euler12
import unittest


class NumberOfFactorsTestCase(unittest.TestCase):
    def test_6_has_4_factors(self):
        self.assertEquals(4, euler12.number_of_factors(6))

    def test_32_has_6_factors(self):
        self.assertEquals(6, euler12.number_of_factors(32))


class FirstTriangleNumberWithNumberOfFactorsTestCase(unittest.TestCase):
    def test_first_triangle_number_with_5_factors_is_28(self):
        self.assertEquals(28, euler12.first_triangle_number_with_number_of_factors(5))


class Euler12TestCase(unittest.TestCase):
    def test_euler12_returns_76576500(self):
        self.assertEquals(76576500, euler12.euler12())
