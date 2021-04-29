def to_jaden_case(string):
    string = string.title().split()
    words = [word.capitalize() for word in string]
    result = ' '.join(words)
    return result


string = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(string))
