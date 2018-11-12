numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh',
           'twelfth']
words = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]
template = "On the {0} day of Christmas my true love gave to me: "


def process(end_verse):
    s = ""
    if end_verse > 1:
        s += ', '.join(words[end_verse - 1:0:-1])
        s += ', and '
    s += words[0]
    return s


def recite(start_verse, end_verse):
    res = []
    while start_verse <= end_verse:
        s = template.format(numbers[start_verse - 1])
        s += process(start_verse)
        res.append(s)
        start_verse += 1
    return res
