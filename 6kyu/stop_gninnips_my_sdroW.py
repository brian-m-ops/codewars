def spin_words(sentence):
    result = ''
    for word in sentence.strip().split():
        if len(word) >= 5:
            result += ''.join(reversed(word)) + ' '
        else:
            result += ''.join(word) + ' '
    return result.strip()


# word != sentence.split()[0]:

sentence = "Welcome"
print(spin_words(sentence))
