import math


def factorial(n):
    if -1 < n < 13:
        return math.factorial(n)
    else:
        raise ValueError('Must be within allowed range of 0-12')


print(factorial(13))
