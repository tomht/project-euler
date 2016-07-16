import euler2
import unittest


class GoldenRatioTestCase(unittest.TestCase):
    def test_golden_ratio_equals_one_point_six_one_eight(self):
        self.assertAlmostEquals(1.618, euler2.GOLDEN_RATIO, 3)


class FibonacciNumberTestCase(unittest.TestCase):
    def test_third_fibonacci_number_is_two(self):
        self.assertEquals(2, euler2.fibonacci_number(3))
    def test_sixth_fibonacci_number_is_eight(self):
        self.assertEquals(8, euler2.fibonacci_number(6))
    def test_tenth_fibonacci_number_is_fifty_five(self):
        self.assertEquals(55, euler2.fibonacci_number(10))


class EvenFibonacciNumberTestCase(unittest.TestCase):
    def test_first_even_fibonacci_number_is_two(self):
        self.assertEquals(2, euler2.even_fibonacci_number(1))
    def test_second_even_fibonacci_number_is_eight(self):
        self.assertEquals(8, euler2.even_fibonacci_number(2))
    def test_third_even_fibonacci_number_is_thirty_four(self):
        self.assertEquals(34, euler2.even_fibonacci_number(3))


class Euler2TestCase(unittest.TestCase):
    def test_euler2_8_is_10(self):
        self.assertEquals(10, euler2.euler2(8))

if __name__ == '__main__':
    unittest.main()
