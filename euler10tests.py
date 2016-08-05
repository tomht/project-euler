import euler10
import unittest


class SumOfPrimesBelowTestCase(unittest.TestCase):
    def test_sum_of_primes_below_10_is_17(self):
        self.assertEquals(17, euler10.sum_of_primes_below(10))


class Euler10TestCase(unittest.TestCase):
    def test_euler10_returns_142913828922(self):
        self.assertEquals(142913828922, euler10.euler10())
