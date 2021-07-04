import re


def reverse_words(text):
    words = re.split(r'(\s+)', text)
    result = []
    [result.append(word[::-1]) for word in words]

    return ''.join(result)


text = 'double  spaced  words'
print(reverse_words(text))
