def number(lines):
    x = []
    [x.append(f"{line+1}: {lines[line]}") for line in range(len(lines))]
    return x
