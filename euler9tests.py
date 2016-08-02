import euler9
import unittest


class PythagoreanTriplesSummingToTestCase(unittest.TestCase):
    def test_pythagorean_triple_summing_to_12_is_3_4_and_5(self):
        self.assertEquals([{'a': 3, 'b': 4, 'c': 5}], euler9.pythagorean_triples_summing_to_(12))


class Euler9TestCase(unittest.TestCase):
    def test_euler9_returns_31875000(self):
        self.assertEquals(31875000, euler9.euler9())
