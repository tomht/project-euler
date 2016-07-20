import euler1
import unittest


class GcdTestCase(unittest.TestCase):
    def test_gcd_11_and_15_is_5(self):
        self.assertEqual(euler1.gcd(10, 15), 5)

    def test_gcd_11_and_13_is_1(self):
        self.assertEqual(euler1.gcd(11, 13), 1)

    def test_gcd_15_and_10_is_5(self):
        self.assertEqual(euler1.gcd(15, 10), 5)

    def test_gcd_1_and_0_is_1(self):
        self.assertEqual(euler1.gcd(1, 0), 1)

    def test_gcd_0_and_1_is_1(self):
        self.assertEqual(euler1.gcd(0, 1), 1)

    def test_gcd_0_and_0_is_0(self):
        self.assertEqual(euler1.gcd(0, 0), 0)

    def test_gcd_minus_10_and_15_is_5(self):
        self.assertEqual(euler1.gcd(-10, 15), 5)

    def test_gcd_10_and_minus_15_is_5(self):
        self.assertEqual(euler1.gcd(10, -15), 5)

    def test_gcd_minus_10_and_minus_15_is_5(self):
        self.assertEqual(euler1.gcd(-10, -15), 5)


class LcmTestCase(unittest.TestCase):
    def test_lcm_2_and_3_is_6(self):
        self.assertEqual(euler1.lcm(2, 3), 6)

    def test_lcm_2_and_4_is_4(self):
        self.assertEqual(euler1.lcm(2, 4), 4)

    def test_lcm_4_and_6_is_12(self):
        self.assertEqual(euler1.lcm(4, 6), 12)

    def test_lcm_3_and_2_is_6(self):
        self.assertEqual(euler1.lcm(3, 2), 6)

    def test_lcm_1_and_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            euler1.lcm(1, 0)


class SumMultiplesOfTestCase(unittest.TestCase):
    def test_multiples_of_2_up_to_10_is_20(self):
        self.assertEqual(euler1.sum_multiples_of(number1=2, limit=10), 20)

    def test_multiples_of_3_up_to_3_is_0(self):
        self.assertEqual(euler1.sum_multiples_of(number1=3, limit=3), 0)

    def test_multiples_of_1_up_to_5_is_10(self):
        self.assertEqual(euler1.sum_multiples_of(number1=1, limit=5), 10)

    def test_multiples_of_0_is_0(self):
        self.assertEqual(euler1.sum_multiples_of(number1=0, limit=1), 0)

    def test_multiples_up_to_0_is_0(self):
        self.assertEqual(euler1.sum_multiples_of(number1=1, limit=0), 0)

    def test_multiples_up_to_limit_less_than_number_is_0(self):
        self.assertEqual(euler1.sum_multiples_of(number1=5, limit=3), 0)

    def test_multiples_up_to_negative_limit_is_0(self):
        self.assertEqual(euler1.sum_multiples_of(number1=2, limit=-8), 0)

    def test_multiples_of_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            euler1.sum_multiples_of(number1=-3, limit=10)

    def test_multiples_of_2_and_3_up_to_10_is_32(self):
        self.assertEqual(32, euler1.sum_multiples_of(number1=2, number2=3, limit=10))

    def test_multiples_of_3_and_5_up_to_20_is_78(self):
        self.assertEqual(78, euler1.sum_multiples_of(number1=3, number2=5, limit=20))

class Euler1TestCase(unittest.TestCase):
    def test_euler1_returns_233168(self):
        self.assertEqual(233168, euler1.euler1())

if __name__ == '__main__':
    unittest.main()
