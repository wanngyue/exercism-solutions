# Decision table of function
# 4	100	400	f
# n	n	n	n
# y	n	n	y
# y	y	n	n
# y	y	y	y

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
