def unique_in_order(iterable):

    if iterable == '':
        return []

    x = [iterable[0]]

    for char in list(iterable[1:]):

        if char != x[-1]:
            x.append(char)
    return x


iterable = ''
print(unique_in_order(iterable))
