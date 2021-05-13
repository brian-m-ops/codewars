def create_phone_number(n):
    string_ints = [str(int) for int in n]
    x = ''.join(string_ints)

    p1 = x[0:3]
    p2 = x[3:6]
    p3 = x[6:10]

    return f"({p1}) {p2}-{p3}"
