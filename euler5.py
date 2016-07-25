def prime_numbers_up_to(number):
    """Return a list of all prime numbers up to a certain number.

    Args:
        number: The limit above which no primes will be returned.
    Returns:
        A list of all primes numbers up to (and including, if prime) number.
    """
    working_list = [True] * number
    working_list[0] = False
    candidate_prime = 2
    while candidate_prime <= number:
        if working_list[candidate_prime - 1]:
            multiple = (candidate_prime * 2) - 1
            while multiple < number:
                working_list[multiple] = False
                multiple += candidate_prime
        candidate_prime += 1
    return [index + 1 for (index, prime) in enumerate(working_list) if prime]

