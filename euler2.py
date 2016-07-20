import math


GOLDEN_RATIO = (1 + math.sqrt(5)) / 2


def fibonacci_number(number):
    return round((GOLDEN_RATIO ** number) / math.sqrt(5))


def even_fibonacci_number(number):
    return fibonacci_number(3 * number)


def euler2(limit):
    sum = 0
    n = 1
    while True:
        fib = even_fibonacci_number(n)
        if fib <= limit:
            sum += fib
            n += 1
        else:
            break
    return sum