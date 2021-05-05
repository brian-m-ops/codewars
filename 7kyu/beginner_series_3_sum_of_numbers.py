def get_sum(a, b):
    high = max(a, b)
    low = min(a, b)
    result = 0

    for number in range(low, high+1):
        result += number
    return result
