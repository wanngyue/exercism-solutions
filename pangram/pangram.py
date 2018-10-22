# def is_pangram(sentence):
#     letters = set()
#     for c in sentence.lower():
#         if c.isalpha():
#             letters.add(c)
#
#     if len(letters) < 26:
#         return False
#     return True
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram(string):
    return ALPHABET.issubset(string.lower())