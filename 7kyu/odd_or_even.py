def odd_or_even(arr):
    if arr == 0 or sum(arr) % 2 == 0:
        return 'even'
    else:
        return 'odd'
