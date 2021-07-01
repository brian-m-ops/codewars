def divisors(integer):
    result = []

    for num in range(2, integer):
        if integer % num == 0:
            result.append(num)

    if len(result) == 0:
        return f'{integer} is prime'

    return result
