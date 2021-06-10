def array_diff(a, b):
    for num in b:
        if num in a:
            for i in range(a.count(num)):
                a.remove(num)
    return a


a = [7, -4, 14, 1, 8, -9, -11, 14, -13, -1, 7, -8, -18, 19]
b = [7, 17, 19, -3, -12, 11, 16, 19, -7, 8]
print(array_diff(a, b))

# if number is in both a and b. Remove from a

# if number is in b. Remove from a
