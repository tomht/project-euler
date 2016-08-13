import shared


def number_of_factors(number, primes=None):
    if primes is None:
        primes = shared.prime_numbers_up_to(number)
    factors = 1
    for prime in primes:
        if number == 1:
            break
        exponent = 0
        while number % prime == 0:
            number = number / prime
            exponent += 1
        factors *= (exponent + 1)
    return factors


def first_triangle_number_with_number_of_factors(factors):
    primes_reference = [2]
    number_of_factors_reference = {1: 1}
    current_number_of_factors = 0
    current_triangle_number_factor1 = 0
    current_triangle_number_factor2 = 0
    index = 0
    even = True
    while current_number_of_factors < factors:
        index += 1
        even = not even
        if even:
            current_triangle_number_factor1 = index / 2
            current_triangle_number_factor2 = index + 1
        else:
            current_triangle_number_factor1 = (index + 1) / 2
            current_triangle_number_factor2 = index
        if current_triangle_number_factor1 not in number_of_factors_reference:
            if primes_reference[-1] < current_triangle_number_factor1:
                primes_reference = shared.prime_numbers_up_to(current_triangle_number_factor1 * 10)
            number_of_factors_reference[current_triangle_number_factor1] \
                = number_of_factors(current_triangle_number_factor1, primes_reference)
        if current_triangle_number_factor2 not in number_of_factors_reference:
            if primes_reference[-1] < current_triangle_number_factor2:
                primes_reference = shared.prime_numbers_up_to(current_triangle_number_factor2 * 10)
            number_of_factors_reference[current_triangle_number_factor2] \
                = number_of_factors(current_triangle_number_factor2, primes_reference)
        current_number_of_factors = number_of_factors_reference[current_triangle_number_factor1] \
                                    * number_of_factors_reference[current_triangle_number_factor2]
    return current_triangle_number_factor1 * current_triangle_number_factor2


def euler12():
    return first_triangle_number_with_number_of_factors(500)
