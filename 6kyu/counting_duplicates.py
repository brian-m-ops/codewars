def duplicate_count(text):
    char_count = {}
    result = 0

    for char in text.lower():
        keys = char_count.keys()
        if char in keys:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for count in char_count.values():
        if count > 1:
            result += 1

    return result
