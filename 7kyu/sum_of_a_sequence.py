def sequence_sum(begin_number, end_number, step):
    result = begin_number

    if begin_number > end_number:
        return 0

    for i in range(begin_number, end_number, step):
        if step + i > end_number:
            break
        else:
            result += i + step

    return result
