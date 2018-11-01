# pattern                           response
# endWith ? and not ALL LETTERS     Sure.
# ALL LETTERS                       Whoa, chill out!
# endWith ? and ALL LETTERS         Calm down, I know what I'm doing!
# without alphabet                  Fine. Be that way!
# else                              Whatever.
def hey(phrase):
    striped_phrase = phrase.strip(' \t\n\r')
    bob_response='Whatever.'
    if len(striped_phrase) == 0:
        bob_response = 'Fine. Be that way!'
    elif striped_phrase.endswith('?'):
        if striped_phrase[:-2].isupper():
            bob_response = 'Calm down, I know what I\'m doing!'
        else:
            bob_response = 'Sure.'
    elif striped_phrase.isupper():
        bob_response = 'Whoa, chill out!'
    return bob_response