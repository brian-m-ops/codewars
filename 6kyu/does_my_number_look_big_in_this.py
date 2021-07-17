def narcissistic(value):
    x = []
    total = 0
    v = list(str(value))

    for i in v:

        x.append(int(i) ** len(v))

    for i in x:
        total += i

    return total == value


print(narcissistic(371))
