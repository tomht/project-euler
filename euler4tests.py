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
