import shared
import unittest


class PrimeNumbersUpToTestCase(unittest.TestCase):
    def test_primes_up_to_10_are_2_3_5_and_7(self):
        self.assertEquals([2, 3, 5, 7], shared.prime_numbers_up_to(10))
