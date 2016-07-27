import Queue


def largest_product_in_number_string(number_string, adjacent_digits):
    """Returns the largest product formed from adjacent characters in a string of digits.

    Args:
        number_string: The string of digits in which to find products.
        adjacent_digits: The number of adjacent digits to include in products.
    Returns:
        The largest product formed from number_string consisting of a number of digits given by adjacent_digits.
    """
    if '0' in number_string:
        number_string_parts = number_string.split('0')
        number_string_part_products = []
        for number_string_part in number_string_parts:
            if len(number_string_part) >= adjacent_digits:
                number_string_part_products.append(
                    largest_product_in_number_string(number_string_part, adjacent_digits))
        return max(number_string_part_products)
    else:
        product_queue = Queue.Queue(adjacent_digits)
        current_product = 1
        largest_product = 1
        for digit in number_string:
            if product_queue.full():
                current_product /= product_queue.get()
            product_queue.put(int(digit))
            current_product *= int(digit)
            largest_product = max(largest_product, current_product)
        return largest_product


def euler8():
    number_string = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace('\n', '').replace('\r', '')
    return largest_product_in_number_string(number_string, 13)
