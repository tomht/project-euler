def SumDigitsOfPowerOf2(power):
    current_power = 0
    current_number = [1]
    while current_power < power:
        next_number = []
        carry = False
        for current_digit in current_number[::-1]:
            next_digit = (current_digit * 2) % 10
            if carry:
                next_digit += 1
            next_number.append(next_digit)
            carry = current_digit >= 5
        if carry:
            next_number.append(1)
        current_number = next_number[::-1]
        current_power += 1
    return sum(current_number)

def euler16():
    return SumDigitsOfPowerOf2(1000)