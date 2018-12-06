from string import punctuation


class Phone(object):
    def __init__(self, phone_number):
        phone_number = ''.join([p for p in phone_number if p.isdigit()])
        if len(phone_number) == 11 and phone_number[0] == '1':
            phone_number = phone_number[1:]
        if len(phone_number) != 10 or int(phone_number[0]) < 2 or int(phone_number[3]) < 2:
            raise ValueError('ERR')
        self.number = phone_number
        self.area_code = phone_number[:3]

    def pretty(self):
        return "({}) {}-{}".format(self.area_code, self.number[3:6], self.number[6:])
