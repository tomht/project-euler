import math


def largest_prime_factor(number):
    candidate_divisor = 2
    largest_prime = 2
    if number <= 1:
        raise ValueError
    while number > 1:
        while number % candidate_divisor == 0:
            number = number / candidate_divisor
            largest_prime = candidate_divisor
        candidate_divisor += 1
    return largest_prime


def euler3():
    return largest_prime_factor(600851475143)
