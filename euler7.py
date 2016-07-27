import math


def nth_prime(n):
    """Returns the nth prime number.

    Args:
        n: The prime number to return.
    Returns:
        The nth prime number.
    """
    primes = [2]
    primes_count = 1
    candidate_prime = 3
    while primes_count < n:
        for prime in primes:
            if prime > math.sqrt(candidate_prime):
                primes.append(candidate_prime)
                primes_count += 1
                break
            if candidate_prime % prime == 0:
                break
        candidate_prime += 1
    return primes[n - 1]


def euler7():
    return nth_prime(10001)
