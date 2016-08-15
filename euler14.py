def longest_collatz_sequence(limit):
    sequence_lengths = [0] * 1000000
    sequence_lengths[0] = 1
    sequence_lengths[1] = 1
    numbers_with_longest_sequence = [1]
    max_sequence_length = 1
    for i in range(limit - 1, 0, -1):
        current_sequence = []
        sequence_length = 1
        sequence_element = i
        while sequence_element >= limit or sequence_lengths[sequence_element] == 0:
            current_sequence.append(sequence_element)
            sequence_length += 1
            if sequence_element % 2 == 0:
                sequence_element = sequence_element / 2
            else:
                sequence_element = 3 * sequence_element + 1
        known_sequence_length = sequence_lengths[sequence_element]
        for (key, value) in enumerate(current_sequence):
            new_sequence_length = known_sequence_length + sequence_length - key
            if value < limit:
                sequence_lengths[value] = new_sequence_length
            if new_sequence_length > max_sequence_length:
                max_sequence_length = new_sequence_length
                numbers_with_longest_sequence = [value]
            elif new_sequence_length == max_sequence_length:
                numbers_with_longest_sequence.append(value)
        if 0 not in sequence_lengths:
            break
    return sorted(numbers_with_longest_sequence)


def euler14():
    return longest_collatz_sequence(1000000)[0]
