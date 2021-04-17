# Very simple, given a number, find its opposite.

def opposite(number):
    if number < 0:
        return abs(number)
    else:
        return number - number * 2

# print(opposite(-7))

# Better solutions

# def opposite(number):
#     return -number

# def opposite(number):
#   return number * -1
