def letters_in_number(number):
    LETTERS_IN_HUNDRED = 7
    LETTERS_IN_THOUSAND = 8
    LETTERS_IN_AND = 3
    atomic_numbers = {
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8,
        20: 6,
        30: 6,
        40: 5,
        50: 5,
        60: 5,
        70: 7,
        80: 6,
        90: 6
    }

    if number < 20:
        return atomic_numbers[number]

    if number < 100 and number % 10 == 0:
        return atomic_numbers[number]

    if number < 100:
        first_part = number - (number % 10)
        second_part = number % 10
        return letters_in_number(first_part) + letters_in_number(second_part)

    if number < 1000 and (number % 100 == 0):
        first_digit = number / 100
        return letters_in_number(first_digit) + LETTERS_IN_HUNDRED

    if number < 1000:
        first_part = (number - (number % 100))
        second_part = number % 100
        return letters_in_number(first_part) + LETTERS_IN_AND + letters_in_number(second_part)

    if number % 1000 == 0:
        first_digit = number / 1000
        return letters_in_number(first_digit) + LETTERS_IN_THOUSAND

    first_part = number - (number % 1000)
    second_part = number % 1000
    return letters_in_number(first_part) + letters_in_number(second_part)


def euler17():
    return sum(map(letters_in_number, range(1, 1001)))
