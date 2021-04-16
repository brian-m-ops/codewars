import math


def high_and_low(numbers):
    nums = numbers.split()
    ints = [int(num) for num in nums]

    return f'{max(ints)} {min(ints)}'


numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

print(high_and_low(numbers))
