class Allergies(object):
    allergies = [
        'eggs',
        'peanuts',
        'shellfish',
        'strawberries',
        'tomatoes',
        'chocolate',
        'pollen',
        'cats'
    ]

    def __init__(self, score):
        self.bits = [int(c) for c in bin(score)[2:].zfill(8)[::-1]]

    def is_allergic_to(self, item):
        return item in self.allergies and self.bits[self.allergies.index(item)]

    @property
    def lst(self):
        return [self.allergies[i] for i, is_allergic in enumerate(self.bits) if is_allergic]
