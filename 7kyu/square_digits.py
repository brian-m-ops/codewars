def square_digits(num):
    square_digits = ([int(digit) ** 2 for digit in str(num)])
    return int(''.join(str(x) for x in square_digits))


print(square_digits(9119))
