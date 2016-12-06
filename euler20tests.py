import euler20
import unittest


class SumOfDigitsTestCase(unittest.TestCase):
    def test_sum_of_digits_of_5_is_5(self):
        self.assertEquals(5, euler20.sum_of_digits(5))

    def test_sum_of_digits_of_12_is_3(self):
        self.assertEquals(3, euler20.sum_of_digits(12))

    def test_sum_of_digits_of_643_is_13(self):
        self.assertEquals(13, euler20.sum_of_digits(643))


class Euler20TestCase(unittest.TestCase):
    def test_euler20_returns_648(self):
        self.assertEquals(648, euler20.euler20())
