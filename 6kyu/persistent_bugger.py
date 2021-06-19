def persistence(n):
    if n < 10:
        return 0

    num_str = str(n)
    result = 1

    for i in num_str:
        result = result * int(i)

    return persistence(result) + 1
