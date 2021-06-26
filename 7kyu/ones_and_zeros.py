def binary_array_to_number(arr):
    result = ''

    for num in arr:
        result += str(num)

    return int(result, 2)
