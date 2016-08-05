def sum_of_primes_below(limit):
    numbers = [True] * (limit + 1)
    numbers[0] = False
    numbers[1] = False
    candidate_prime = 2
    while candidate_prime < limit:
        if numbers[candidate_prime]:
            prime = candidate_prime
            index = 2
            product = prime * index
            while product <= limit:
                numbers[product] = False
                index += 1
                product = prime * index
        candidate_prime += 1
    primes_sum = 0
    for number, is_prime in enumerate(numbers):
        if is_prime:
            primes_sum += number
    return primes_sum


def euler10():
    return sum_of_primes_below(2000000)
