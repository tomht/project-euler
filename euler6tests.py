import euler6
import unittest


class SumSquareDifferenceTestCase(unittest.TestCase):
    def test_sum_square_difference_of_10_is_2640(self):
        self.assertEquals(2640, euler6.sum_square_difference(10))


class Euler6TestCase(unittest.TestCase):
    def test_euler6_returns_25164150(self):
        self.assertEquals(25164150, euler6.euler6())
