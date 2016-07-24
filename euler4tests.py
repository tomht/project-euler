import euler4
import unittest


class IsPalindromeTestCase(unittest.TestCase):
    def test_131_is_palindrome(self):
        self.assertTrue(euler4.is_palindrome(131))

    def test_6776_is_palindrome(self):
        self.assertTrue(euler4.is_palindrome(6776))

    def test_5_is_palindrome(self):
        self.assertTrue(euler4.is_palindrome(5))

    def test_10_is_not_palindrome(self):
        self.assertFalse(euler4.is_palindrome(10))


class LargestPalindromeProductTestCase(unittest.TestCase):
    def test_largest_palindrome_product_of_1_digit_numbers_is_9(self):
        self.assertEquals(9, euler4.largest_palindrome_product(1))
    def test_largest_palindrome_product_of_2_digit_numbers_is_9009(self):
        self.assertEquals(9009, euler4.largest_palindrome_product(2))
