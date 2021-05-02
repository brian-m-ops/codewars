def is_isogram(string):
    if len(list(string.lower())) == len(set(string.lower())) or string == '':
        return True
    else:
        return False
