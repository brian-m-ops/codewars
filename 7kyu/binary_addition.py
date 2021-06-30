def add_binary(a, b):
    return str(bin(int(bin(a), 2) + int(bin(b), 2)))[2:]


print(add_binary(1, 1))
