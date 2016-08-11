import euler11
import unittest


class Euler11TestCase(unittest.TestCase):
    def test_euler11_returns_70600674(self):
        self.assertEquals(70600674, euler11.euler11())
