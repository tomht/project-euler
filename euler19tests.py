import euler19
import unittest
from datetime import *


class SundaysOn1stOfMonthTestCase(unittest.TestCase):
    def test_1_sunday_on_1st_of_month_in_2016(self):
        self.assertEquals(1, euler19.sundays_on_1st_of_month(date(2016, 1, 1), date(2016, 12, 31)))


class Euler19TestCase(unittest.TestCase):
    def test_euler19_returns_171(self):
        self.assertEquals(171, euler19.euler19())
