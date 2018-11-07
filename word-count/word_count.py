import re

def word_count(phrase):
    phrase = phrase.lower().strip().replace('_', ' ')
    words = re.findall(r"[\w']+", phrase)
    d = {}
    for word in set(words):
        i = d.get(word.strip('\''), 0)
        d[word.strip('\'')] = i + words.count(word)
    return d
