import math


def gcd(number1, number2):
    n = abs(number1)
    m = abs(number2)
    while n > 0 and m > 0:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n + m


def lcm(number1, number2):
    if number1 * number2 == 0:
        raise ValueError
    return (number1 * number2) / gcd(number1, number2)


def sum_multiples_of(number1, number2=None, limit=0):
    if number2 is not None:
        return sum_multiples_of(number1=number1, limit=limit) \
               + sum_multiples_of(number1=number2, limit=limit) \
               - sum_multiples_of(number1=lcm(number1, number2), limit=limit)
    else:
        if number1 < 0:
            raise ValueError
        if limit < 0:
            return 0
        if number1 == 0:
            return 0
        sequence_limit = math.floor((limit - 1) / number1)
        return (number1 * sequence_limit * (sequence_limit + 1)) / 2


def euler1():
    return sum_multiples_of(3, 5, 1000)
