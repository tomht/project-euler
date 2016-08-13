import shared


def lowest_common_multiple_of_numbers_up_to(number):
    """Return the lowest common multiple of all numbers up to and including a particular number.

    Args:
        number: The number to find the LCM of all numbers up to.
    Returns:
        The LCM of all numbers up to and including number.
    """
    lcm = 1
    primes_up_to_number = shared.prime_numbers_up_to(number)
    for prime in primes_up_to_number:
        exponent = 1
        prime_power = prime ** exponent
        while prime_power <= number:
            exponent += 1
            prime_power = prime ** exponent
        lcm *= prime ** (exponent - 1)
    return lcm


def euler5():
    return lowest_common_multiple_of_numbers_up_to(20)
