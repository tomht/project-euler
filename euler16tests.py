import euler16
import unittest

class SumDigitsOfPowerOf2TestCase(unittest.TestCase):
    def test_power_is_15_sum_is_26(self):
        self.assertEquals(26, euler16.SumDigitsOfPowerOf2(15))

class Euler16TestCase(unittest.TestCase):
    def test_euler16_returns_1366(self):
        self.assertEquals(1366, euler16.euler16())