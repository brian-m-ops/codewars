def duplicate_encode(word):
    x = list(word.lower())

    result = []
    for letter in x:
        if x.count(letter) < 2:
            result.append("(")
        else:
            result.append(")")

    return ''.join(result)


word = "Success"  # ")())())","should ignore case"

print(duplicate_encode(word))
