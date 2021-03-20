"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""


def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_str = list(string)
    result = []
    result_str = ""

    for letter in new_str:
        if letter not in vowels:
            result.append(letter)

    return result_str.join(result)


# Test
print(disemvowel('test'))
print(disemvowel('TEST'))

# Better ways
# 1
# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")

# 2
# def disemvowel(string):
#     return "".join(c for c in string if c.lower() not in "aeiou")

# 3
# def disemvowel(s):
#     for i in "aeiouAEIOU":
#         s = s.replace(i,'')
#     return s
