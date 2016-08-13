import euler12
import unittest


class Euler12TestCase(unittest.TestCase):
    def test_euler12_returns_76576500(self):
        self.assertEquals(76576500, euler12.euler12())
