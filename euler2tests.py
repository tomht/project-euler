import euler2
import unittest


class GoldenRatioTestCase(unittest.TestCase):
    def test_golden_ratio_equals_1_point_618(self):
        self.assertAlmostEquals(1.618, euler2.GOLDEN_RATIO, 3)


class FibonacciNumberTestCase(unittest.TestCase):
    def test_3rd_fibonacci_number_is_2(self):
        self.assertEquals(2, euler2.fibonacci_number(3))

    def test_6th_fibonacci_number_is_8(self):
        self.assertEquals(8, euler2.fibonacci_number(6))

    def test_10th_fibonacci_number_is_55(self):
        self.assertEquals(55, euler2.fibonacci_number(10))


class EvenFibonacciNumberTestCase(unittest.TestCase):
    def test_1st_even_fibonacci_number_is_2(self):
        self.assertEquals(2, euler2.even_fibonacci_number(1))

    def test_2nd_even_fibonacci_number_is_8(self):
        self.assertEquals(8, euler2.even_fibonacci_number(2))

    def test_3rd_even_fibonacci_number_is_34(self):
        self.assertEquals(34, euler2.even_fibonacci_number(3))


class SumEvenFibonacciNumbersUpToTestCase(unittest.TestCase):
    def test_sum_of_even_fibonacci_numbers_up_to_150_is_188(self):
        self.assertEquals(188, euler2.sum_even_fibonacci_numbers_up_to(150))


class Euler2TestCase(unittest.TestCase):
    def test_euler2_returns_4613732(self):
        self.assertEquals(4613732, euler2.euler2())


if __name__ == '__main__':
    unittest.main()
