#Decision table of function
# 4	100	400	f
# n	n	n	n
# y	n	n	y
# y	y	n	n
# y	y	y	y

def is_leap_year(year):
    isLeapYear = True

    if year%4 != 0 or (year%100 == 0 and year%400 !=0):
        isLeapYear=False
    return isLeapYear




