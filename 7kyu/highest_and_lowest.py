import math


def high_and_low(numbers):

    nums = [int(num) for num in numbers.split()]

    return f'{max(nums)} {min(nums)}'


numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

print(high_and_low(numbers))
