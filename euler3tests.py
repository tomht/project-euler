import euler3
import unittest


class LargestPrimeFactorTestCase(unittest.TestCase):
    def test_largest_prime_factor_of_10_is_5(self):
        self.assertEquals(5, euler3.largest_prime_factor(10))

    def test_largest_prime_factor_of_1300_is_13(self):
        self.assertEquals(13, euler3.largest_prime_factor(1300))

    def test_largest_prime_factor_of_97_is_97(self):
        self.assertEquals(97, euler3.largest_prime_factor(97))

    def test_largest_prime_factor_of_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            euler3.largest_prime_factor(1)


class Euler3TestCase(unittest.TestCase):
    def test_euler3_returns_6857(self):
        self.assertEquals(6857, euler3.euler3())


if __name__ == '__main__':
    unittest.main()
