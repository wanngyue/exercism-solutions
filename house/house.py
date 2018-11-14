words = [
    "the house that Jack built.",
    "the malt that lay in ",
    "the rat that ate ",
    "the cat that killed ",
    "the dog that worried ",
    "the cow with the crumpled horn that tossed ",
    "the maiden all forlorn that milked ",
    "the man all tattered and torn that kissed ",
    "the priest all shaven and shorn that married ",
    "the rooster that crowed in the morn that woke ",
    "the farmer sowing his corn that kept ",
    "the horse and the hound and the horn that belonged to ",
]


def recite(start_verse, end_verse):
    l = []
    if start_verse == end_verse:
        l.append("This is {0}".format(''.join(words[start_verse-1::-1])))
    else:
        l.extend(recite(start_verse, end_verse - 1))
        l.extend(recite(end_verse, end_verse))
    return l
