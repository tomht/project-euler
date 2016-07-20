import euler1
import unittest


class GcdTestCase(unittest.TestCase):
    def test_gcd_ten_and_fifteen_is_five(self):
        self.assertEqual(euler1.gcd(10, 15), 5)

    def test_gcd_eleven_and_thirteen_is_one(self):
        self.assertEqual(euler1.gcd(11, 13), 1)

    def test_gcd_fifteen_and_ten_is_five(self):
        self.assertEqual(euler1.gcd(15, 10), 5)

    def test_gcd_one_and_zero_is_one(self):
        self.assertEqual(euler1.gcd(1, 0), 1)

    def test_gcd_zero_and_one_is_one(self):
        self.assertEqual(euler1.gcd(0, 1), 1)

    def test_gcd_zero_and_zero_is_zero(self):
        self.assertEqual(euler1.gcd(0, 0), 0)

    def test_gcd_minus_ten_and_fifteen_is_five(self):
        self.assertEqual(euler1.gcd(-10, 15), 5)

    def test_gcd_ten_and_minus_fifteen_is_five(self):
        self.assertEqual(euler1.gcd(10, -15), 5)

    def test_gcd_minus_ten_and_minus_fifteen_is_five(self):
        self.assertEqual(euler1.gcd(-10, -15), 5)


class LcmTestCase(unittest.TestCase):
    def test_lcm_two_and_three_is_six(self):
        self.assertEqual(euler1.lcm(2, 3), 6)

    def test_lcm_two_and_four_is_four(self):
        self.assertEqual(euler1.lcm(2, 4), 4)

    def test_lcm_four_and_six_is_twelve(self):
        self.assertEqual(euler1.lcm(4, 6), 12)

    def test_lcm_three_and_two_is_six(self):
        self.assertEqual(euler1.lcm(3, 2), 6)

    def test_lcm_one_and_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            euler1.lcm(1, 0)


class SumMultiplesOfTestCase(unittest.TestCase):
    def test_multiples_of_two_up_to_ten_is_twenty(self):
        self.assertEqual(euler1.sum_multiples_of(number1=2, limit=10), 20)

    def test_multiples_of_three_up_to_three_is_zero(self):
        self.assertEqual(euler1.sum_multiples_of(number1=3, limit=3), 0)

    def test_multiples_of_one_up_to_five_is_ten(self):
        self.assertEqual(euler1.sum_multiples_of(number1=1, limit=5), 10)

    def test_multiples_of_zero_is_zero(self):
        self.assertEqual(euler1.sum_multiples_of(number1=0, limit=1), 0)

    def test_multiples_up_to_zero_is_zero(self):
        self.assertEqual(euler1.sum_multiples_of(number1=1, limit=0), 0)

    def test_multiples_up_to_limit_less_than_number_is_zero(self):
        self.assertEqual(euler1.sum_multiples_of(number1=5, limit=3), 0)

    def test_multiples_up_to_negative_limit_is_zero(self):
        self.assertEqual(euler1.sum_multiples_of(number1=2, limit=-8), 0)

    def test_multiples_of_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            euler1.sum_multiples_of(number1=-3, limit=10)

    def test_multiples_of_two_and_three_up_to_ten_is_thirty_two(self):
        self.assertEqual(32, euler1.sum_multiples_of(number1=2, number2=3, limit=10))

    def test_multiples_of_three_and_five_up_to_twenty_is_seventy_eight(self):
        self.assertEqual(78, euler1.sum_multiples_of(number1=3, number2=5, limit=20))

class Euler1TestCase(unittest.TestCase):
    def test_euler1_returns_233168(self):
        self.assertEqual(233168, euler1.euler1())

if __name__ == '__main__':
    unittest.main()
