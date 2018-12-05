l = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
     "eleven", "twelve", "thirteen", 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
l10 = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError('err')
    if number <= 20:
        return l[number]
    if number < 100:
        return '-'.join([l10[number // 10], l[number % 10]])
    if number < 1000:
        r = l[number // 100] + ' ' + 'hundred'
        if number % 100 != 0:
            r = r + ' and ' + say(number % 100)
        return r
    if number < 1e6:
        r = say(int(number / 1000)) + ' ' + 'thousand'
        if number % 1000 != 0:
            r = r + ' ' + say(number % 1000)
        return r
    if number < 1e9:
        r = say(int(number / 1e6)) + ' ' + 'million'
        if number % 1e6 != 0:
            r = r + ' ' + say(number % 1000_000)
        return r
    if number < 1e12:
        r = say(int(number / 1e9)) + ' ' + 'billion'
        if number % 1e9 != 0:
            r = r + ' ' + say(int(number % 1e9))
        return r
