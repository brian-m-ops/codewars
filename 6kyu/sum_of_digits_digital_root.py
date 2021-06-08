# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    digits = [int(x) for x in str(n)]

    result = 0

    for nums in digits:
        result += nums

    if len(str(result)) != 1:
        return digital_root(result)

    return result


n = 493193
print(digital_root(n))
