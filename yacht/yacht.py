# Score categories
# Change the values as you see fit
# Ones	            Any combination
# Twos        	    Any combination
# Threes	        Any combination
# Fours       	    Any combination
# Fives	            Any combination
# Sixes	            Any combination
# Full House	    Three of one number and two of another
# Four-Of-A-Kind	At least four dice showing the same face
# Little Straight	1-2-3-4-5
# Big Straight	    2-3-4-5-6
# Choice	        Any combination
# Yacht	            All five dice showing the same face

# refer to https://pythex.org/
import re

YACHT = '(([1-6])\\2{4})'
ONES = '1+'
TWOS = '2+'
THREES = '3+'
FOURS = '4+'
FIVES = '5+'
SIXES = '6+'
FULL_HOUSE = '[1-6]{5}'
FOUR_OF_A_KIND = '([1-6])\\1{3}'
LITTLE_STRAIGHT = '12345'
BIG_STRAIGHT = '23456'
CHOICE = '[1-6]*'


def score(dice, category):
    dice = sorted(dice)
    d_str = ''.join([str(d) for d in dice])
    res = 0
    if re.search(category, d_str):
        if category == YACHT:
            res = 50
        elif category == ONES or category == TWOS or category == THREES or category == FOURS or category == FIVES or category == SIXES:
            res = dice.count(int(category[0])) * int(category[0])
        elif category == FULL_HOUSE:
            if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
                res = sum(dice)
        elif category == FOUR_OF_A_KIND:
            res = (dice[0] * 4 if dice.count(dice[0]) == 4 else dice[4] * 4)
        elif category == LITTLE_STRAIGHT or category == BIG_STRAIGHT:
            res = 30
        else:
            res = sum(dice)
    return res
