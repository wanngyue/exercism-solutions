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
    phrase = phrase.strip()
    if not phrase:
        return 'Fine. Be that way!'
    elif is_question(phrase) and is_yelling(phrase):
        return 'Calm down, I know what I\'m doing!'
    elif is_question(phrase):
        return 'Sure.'
    elif is_yelling(phrase):
        return 'Whoa, chill out!'
    return 'Whatever.'
