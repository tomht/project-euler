import euler7
import unittest


class NthPrimeTestCase(unittest.TestCase):
    def test_6th_prime_is_13(self):
        self.assertEquals(13, euler7.nth_prime(6))


class Euler7TestCase(unittest.TestCase):
    def test_euler7_returns_104743(self):
        self.assertEquals(104743, euler7.euler7())
