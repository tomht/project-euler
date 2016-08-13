import euler11
import unittest


class MaxProductInGridTestCase(unittest.TestCase):
    sample_grid = [[1, 2, 1, 4], [2, 1, 3, 1], [1, 2, 2, 2], [1, 2, 1, 2]]

    def test_max_product_in_sample_grid_is_24(self):
        self.assertEquals(24, euler11.max_product_in_grid(MaxProductInGridTestCase.sample_grid))


class Euler11TestCase(unittest.TestCase):
    def test_euler11_returns_70600674(self):
        self.assertEquals(70600674, euler11.euler11())
