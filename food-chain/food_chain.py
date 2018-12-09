animals = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']
lyric = ["I don't know why she swallowed the fly. Perhaps she'll die.",
         "It wriggled and jiggled and tickled inside her.",
         "How absurd to swallow a bird!",
         "Imagine that, to swallow a cat!",
         "What a hog, to swallow a dog!",
         "Just opened her throat and swallowed a goat!",
         "I don't know how she swallowed a cow!",
         "She's dead, of course!"
         ]
f = "I know an old lady who swallowed a {}."
f1 = "She swallowed the {0} to catch the {1}."


def recite(start_verse, end_verse):
    recites = []
    while start_verse <= end_verse:
        recites += [f.format(animals[start_verse - 1])]
        if 1 < start_verse < 8:
            recites += [lyric[start_verse - 1]]
            for i in range(start_verse - 1):
                animal = animals[start_verse - 1 - i - 1];
                if animal == 'spider':
                    animal = animal + " that wriggled and jiggled and tickled inside her"
                recites += [f1.format(animals[start_verse - 1 - i], animal)]
        if start_verse == 8:
            recites.append("She's dead, of course!")
        else:
            recites += [lyric[0]]
        if end_verse != start_verse:
            recites += [""]
        start_verse += 1
    return recites
