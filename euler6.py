def sum_square_difference(number):
    """Return the difference between the square of the sum of the consecutive integers up to a number, and the sum of
    the squares of the consecutive integers up to the same number.

    Args:
        number: The number of consecutive integers (starting from 1) to include in the sum.
    Returns:
        The difference between the square of the sum of the consecutive integers up to number, and the sum of the
        squares of the consecutive integers up to number.
    """
    return ((3 * (number ** 4)) + (2 * (number ** 3)) - (3 * (number ** 2)) - (2 * number)) / 12


def euler6():
    return sum_square_difference(100)
