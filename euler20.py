import math


def sum_of_digits(number):
    sum = 0
    working = number
    while working >= 1:
        sum += working % 10
        working /= 10
    return sum


def euler20():
    return sum_of_digits(math.factorial(100))
