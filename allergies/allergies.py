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
        self.lst = [allergen for i, allergen in enumerate(self.allergies) if (score & (1 << i))]

    def is_allergic_to(self, item):
        return item in self.lst
