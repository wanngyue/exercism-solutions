from datetime import date
from datetime import timedelta

week_l = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
delta = timedelta(days=1)
dict = {
    '1st': 1,
    '2nd': 2,
    '3rd': 3,
    '4th': 4,
    '5th': 5,
}


def f(n, d, index):
    for i in range(n):
        d = d + delta
        while d.weekday() != index:
            tmp = d + delta
            if tmp.month != d.month:
                raise MeetupDayException("test")
            d = tmp
    return d


def meetup_day(year, month, day_of_the_week, which):
    index = week_l.index(day_of_the_week)
    d = date(year, month, 12)
    if which == 'teenth':
        return f(1, d, index)
    d = date(year, month, 1) - delta
    if which == 'last':
        d = date(year + (month + 1) // 13, (month + 1) % 12 if month != 11 else 12, 1) - delta
        while d.weekday() != index:
            d -= delta
        return d
    return f(dict[which], d, index)


class MeetupDayException(Exception):
    def __init__(self, message):
        self.message = message
        self.args = {message}
