def find_outlier(integers):
    odd = []
    even = []

    for num in integers:
        if num % 2 == 0:
            even.append(num)
        if num % 2 != 0:
            odd.append(num)

    if len(even) > len(odd):
        return odd[0]
    else:
        return even[0]


integers = [2, 4, 6, 8, 10, 3]

print(find_outlier(integers))

# Better way
# def find_outlier(int):
    # odds = [x for x in int if x%2!=0]
    # evens= [x for x in int if x%2==0]
    # return odds[0] if len(odds)<len(evens) else evens[0]