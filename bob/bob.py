# pattern                           response
# endWith ? and not ALL LETTERS     Sure.
# ALL LETTERS                       Whoa, chill out!
# endWith ? and ALL LETTERS         Calm down, I know what I'm doing!
# without alphabet                  Fine. Be that way!
# else                              Whatever.
def is_yelling(phrase):
    return phrase.isupper()


def is_question(phrase):
    return phrase.endswith('?')


def hey(phrase):
    striped_phrase = phrase.strip(' \t\n\r')
    if len(striped_phrase) == 0:
        return 'Fine. Be that way!'
    elif is_question(striped_phrase):
        if is_yelling(striped_phrase[:-2]):
            return 'Calm down, I know what I\'m doing!'
        else:
            return 'Sure.'
    elif is_yelling(striped_phrase):
        return 'Whoa, chill out!'
    return 'Whatever.'
