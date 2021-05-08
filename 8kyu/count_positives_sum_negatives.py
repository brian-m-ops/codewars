def count_positives_sum_negatives(arr):
    neg = []
    pos = []
    result = []

    if arr == []:
        return result

    for num in arr:

        if num > 0:
            pos.append(num)
        elif num < 0:
            neg.append(num)

    result.append(len(pos))
    result.append(sum(neg))

    return result
