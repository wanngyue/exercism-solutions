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
        self.lst = [allergen for allergen in self.allergies if (score & (1 << self.allergies.index(allergen)))]

    def is_allergic_to(self, item):
        return item in self.lst

