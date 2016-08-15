import euler14
import unittest


class LongestCollatzSequenceTestCase(unittest.TestCase):
    def test_longest_collatz_sequence_below_4_is_3(self):
        self.assertEquals([3], euler14.longest_collatz_sequence(4))


class Euler14TestCase(unittest.TestCase):
    def test_euler14_returns_837799(self):
        self.assertEquals(837799, euler14.euler14())
