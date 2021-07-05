from string import ascii_lowercase

letters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
text = "The sunset sets at twelve o' clock."


def alphabet_position(text):
    x = list(text.lower())
    result = ''

    for char in x:
        if char in letters:
            result += letters[char]
            result += ' '

    return result.strip()


print(alphabet_position(text))
