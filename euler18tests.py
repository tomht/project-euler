import euler18
import unittest


class MaxPathTestCase(unittest.TestCase):
    def test_sample_triangle_returns_23(self):
        sample_triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        self.assertEquals(23, euler18.max_path(sample_triangle))


class Euler18TestCase(unittest.TestCase):
    def test_euler18_returns_1074(self):
        self.assertEquals(1074, euler18.euler18())
