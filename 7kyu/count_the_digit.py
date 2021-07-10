def nb_dig(n, d):
    result = 0
    for k in range(n + 1):
        num = str(k * k)
        if str(d) in num:
            result += num.count(str(d))
    return result