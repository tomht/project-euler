import math

GOLDEN_RATIO = (1 + math.sqrt(5)) / 2


def fibonacci_number(number):
    """Return the specified Fibonacci number.

    Args:
        number: The position of the Fibonacci number to return.
    Returns:
        The element of the Fibonacci sequence in the position given by number.
    """
    return round((GOLDEN_RATIO ** number) / math.sqrt(5))


def even_fibonacci_number(number):
    """Return the specified even Fibonacci number.

    Args:
        number: The position of the even Fibonacci number to return.
    Returns:
        The element of the sequence of even Fibonacci numbers in the position given by number.
    """
    return fibonacci_number(3 * number)


def sum_even_fibonacci_numbers_up_to(limit):
    """Return the sum of even Fibonacci numbers less than or equal to a limit.

    Args:
        limit: The number above which no even Fibonacci numbers should be summed.
    Returns:
        The sum of even Fibonacci numbers less than or equal to limit.
    """
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


def euler2():
    return sum_even_fibonacci_numbers_up_to(4000000)
