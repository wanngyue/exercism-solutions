op_mapping = {
    'plus': '+',
    'minus': '-',
    'multiplied': '*',
    'divided': '//'
}


def calculate(question):
    if '?' not in question or 'What is ' not in question:
        raise ValueError('ERR')
    words = question.strip('?').strip('What is ').replace('divided by', 'divided').replace('multiplied by',
                                                                                           'multiplied').split()
    try:
        first = words[0]
        res = int(first)
        i = 1
        while i < len(words):
            op = op_mapping[words[i]]
            second = words[i + 1]
            res = eval(first + op + second)
            first = str(res)
            i += 2
    except:
        raise ValueError('ERR')
    return res
