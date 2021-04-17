# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    input_list = list(input_str)

    for vowel in input_list:
        if vowel in vowels:
            num_vowels += len(vowel)

    return num_vowels


# print(get_count('abcde'))

# Better ways
# 1
# import re
# def getCount(str):
#     return len(re.findall('[aeiou]', str, re.IGNORECASE))

# 2
# def getCount(s):
#     return sum(c in 'aeiou' for c in s)
