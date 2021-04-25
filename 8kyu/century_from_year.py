def century(year):

    if year % 100 == 0:
        result = year // 100
    else:
        result = year // 100 + 1

    return result
