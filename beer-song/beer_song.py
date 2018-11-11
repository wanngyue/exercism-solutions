def recite(start, take=1):
    str = []
    while start >= 0 and take > 0:
        if start == 0:
            str.append("No more bottles of beer on the wall, no more bottles of beer.")
            str.append("Go to the store and buy some more, "
                       "99 bottles of beer on the wall.")
        elif start == 1:
            str.append("1 bottle of beer on the wall, 1 bottle of beer.")
            str.append("Take it down and pass it around, "
                       "no more bottles of beer on the wall.")

        else:
            c = 's'
            if start == 2:
                c = ''
            str.append("{0} bottles of beer on the wall, {0} bottles of beer.".format(start))
            str.append("Take one down and pass it around, {0} bottle{1} of beer on the wall.".format(start - 1, c))
        str.append("")
        take -= 1
        start -= 1
    return str[:-1]
