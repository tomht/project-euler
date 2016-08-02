import math


def pythagorean_triples_summing_to_(triple_sum):
    triples = []
    if triple_sum % 2 != 0:
        return triples
    # Find pairs of integers m and n such that m > n and m*(m+n) is equal to half the triple_sum.
    for m in range(int(math.ceil(math.sqrt(triple_sum / 4))), int(math.ceil(math.sqrt(triple_sum / 2)))):
        if (triple_sum / 2) % m == 0:
            n = (triple_sum / (2 * m)) - m
            a = (m ** 2) - (n ** 2)
            b = 2 * m * n
            c = (m ** 2) + (n ** 2)
            triples.append({'a': a, 'b': b, 'c': c})
    return triples


def euler9():
    triple = pythagorean_triples_summing_to_(1000)[0]
    return triple['a'] * triple['b'] * triple['c']
