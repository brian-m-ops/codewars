import string


def is_pangram(s):
    alphabet_string = string.ascii_lowercase
    new_s = list(s.lower())
    result = []
    for character in new_s:
        if character in alphabet_string and character in new_s and character not in result:
            result.append(character)
    if len(result) == 26:
        return True
    else:
        return False
