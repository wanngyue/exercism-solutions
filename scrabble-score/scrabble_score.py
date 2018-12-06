d = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}

def score(word):
    sum = 0
    for letter in word.upper():
        for k, l in d.items():
            if letter in k:
                sum += l
                break
    return sum
