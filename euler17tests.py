import euler17
import unittest


class LettersInNumberTestCase(unittest.TestCase):
    def test_1_has_3_letters(self):
        self.assertEquals(3, euler17.letters_in_number(1))

    def test_11_has_6_letters(self):
        self.assertEquals(6, euler17.letters_in_number(11))

    def test_23_has_11_letters(self):
        self.assertEquals(11, euler17.letters_in_number(23))

    def test_115_has_20_letters(self):
        self.assertEquals(20, euler17.letters_in_number(115))

    def test_342_has_23_letters(self):
        self.assertEquals(23, euler17.letters_in_number(342))

    def test_1289_has_34_letters(self):
        self.assertEquals(34, euler17.letters_in_number(1289))


class Euler17TestCase(unittest.TestCase):
    def test_euler17_returns_21124(self):
        self.assertEquals(21124, euler17.euler17())
