def DNA_strand(dna):
    result = []

    for symbol in dna:
        if symbol == "A":
            result += "T"
        elif symbol == "T":
            result += "A"
        elif symbol == "C":
            result += "G"
        elif symbol == "G":
            result += "C"
    result = ''.join(result)
    return result
