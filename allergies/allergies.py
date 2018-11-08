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
        self.l = [self.allergies[i] for i in range(8) if (score & (1 << i))]

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return self.l
