def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if
            len(word) == len(candidate) and word.upper() != candidate.upper() and
            sorted(word.upper()) == sorted(candidate.upper())]
