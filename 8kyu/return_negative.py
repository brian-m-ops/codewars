def make_negative(number):
    if number == 0:
        return 0
    elif number < 0:
        return number
    else:
        return number - number * 2

# Better way
# return -abs(number)
