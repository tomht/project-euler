import euler15
import unittest


class PathsThroughLatticeTestCase(unittest.TestCase):
    def test_6_paths_through_lattice_size_2(self):
        self.assertEquals(6, euler15.paths_through_lattics(2))


class Euler15TestCase(unittest.TestCase):
    def test_euler15_returns_137846528820(self):
        self.assertEquals(137846528820, euler15.euler15())
