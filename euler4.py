import math


def is_palindrome(number):
    working_number = number
    reversed_number = 0
    while working_number > 0:
        next_digit = working_number % 10
        reversed_number = (reversed_number * 10) + next_digit
        working_number = math.floor(working_number / 10)
    return reversed_number == number



def largest_palindrome_product(digits):
    """Return the largest palindromic number equal to the product of two numbers with a particular number of digits in
    base 10.

    Args:
        digits: The number of digits in the multiplicands of the palindrome product.
    Returns:
        The largest palindromic number equal to the product of two numbers with the number of digits specified by the
        digits variable.
    """
    largest_n_digit_number = 10 ** digits - 1
    smallest_n_digit_number = 10 ** (digits - 1)
    i = largest_n_digit_number
    j = largest_n_digit_number
    while i >= smallest_n_digit_number:
        while j >= i:
            current_product = i * j
            if is_palindrome(current_product):
                return current_product
            j -= 1
        i -= 1
        j = largest_n_digit_number
    return None
