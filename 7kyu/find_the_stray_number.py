def stray(arr):
    for num in arr:
        if not arr.count(num) > 1:
            return num


arr = [17, 17, 3, 17, 17, 17, 17]
print(stray(arr))