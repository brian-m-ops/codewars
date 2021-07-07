def tribonacci(signature, n):
    count = 0
    n1 = signature[0]
    n2 = signature[1]
    n3 = signature[2]
    result = signature

    if n == 0:
        return []
    elif n == 1:
        return [n1]
    elif n == 2:
        return [n1, n2]
    else:
        while count < n - 3:
            nth = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = nth
            count += 1
            result.append(nth)

    return result


signature = [1, 1, 1]
n = 10
print(tribonacci(signature, 10))
