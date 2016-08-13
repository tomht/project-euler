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
    return 0


def euler12():
    return 0
