import euler5
import unittest


class LowestCommonMultipleOfNumbersUpToTestCase(unittest.TestCase):
    def test_lcm_of_numbers_up_to_10_is_2520(self):
        self.assertEquals(2520, euler5.lowest_common_multiple_of_numbers_up_to(10))


class Euler5TestCase(unittest.TestCase):
    def test_euler5_returns_232792560(self):
        self.assertEquals(232792560, euler5.euler5())
