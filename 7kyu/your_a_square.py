
import math


def is_square(n):
    if n == 0:
        return True
    if n < 0:
        return False

    for num in range(n):
        sqrt = math.isqrt(n)

        if sqrt * sqrt == n:
            return True
        else:
            return False


print(is_square(25))
