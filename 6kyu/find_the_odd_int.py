def find_it(seq):
    result = 0
    for num in seq:
        if seq.count(num) % 2 != 0:
            result = num
    return result
