def count_bits(n):
    result = 0
    for digit in list(bin(n)):
        if digit == '1':
            result += 1
    return result


print(count_bits(10))  # Should equal 2
