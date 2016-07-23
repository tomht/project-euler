import math


def is_palindrome(number):
    working_number = number
    reversed_number = 0
    while working_number > 0:
        next_digit = working_number % 10
        reversed_number = (reversed_number * 10) + next_digit
        working_number = math.floor(working_number / 10)
    return reversed_number == number
