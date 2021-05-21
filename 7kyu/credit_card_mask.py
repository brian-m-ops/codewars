# return masked string
def maskify(cc):
    lst = list(cc)
    result = ""

    for num in lst:
        result += str(num)

    unmasked = result[-4:]
    masked = len(result) - len(unmasked)
    x = masked * "#"

    return x + unmasked


cc = "4556364607935616"

print(maskify(cc))
