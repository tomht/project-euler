import euler13
import unittest


class NumberOfDigitsTestCase(unittest.TestCase):
    def test_1_has_1_digit(self):
        self.assertEquals(1, euler13.number_of_digits(1))

    def test_10_has_2_digits(self):
        self.assertEquals(2, euler13.number_of_digits(10))

    def test_100_has_3_digit(self):
        self.assertEquals(3, euler13.number_of_digits(100))


class FirstDigitsTestCase(unittest.TestCase):
    def test_first_digit_of_10_is_1(self):
        self.assertEquals(1, euler13.first_digits(10, 1))


class FirstDigitsOfSumTestCase(unittest.TestCase):
    sample_list = [238, 537, 667, 321, 909]

    def test_first_two_digits_of_sum_of_sample_list_is_26(self):
        self.assertEquals(26, euler13.first_digits_of_sum(2, FirstDigitsOfSumTestCase.sample_list))


class Euler13TestCase(unittest.TestCase):
    def test_euler13_returns_5537376230(self):
        self.assertEquals(5537376230, euler13.euler13())
