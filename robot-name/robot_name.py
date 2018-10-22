from string import ascii_uppercase as letters
from string import digits
import random

def getRandomName():
    random.seed()
    name = ""
    for i in range(0, 2):
        name += random.choice(letters)
    for i in range(0, 3):
        name += random.choice(digits)
    return name


class Robot(object):
    def __init__(self):
        Robot.reset(self)

    def reset(self):
        self.name = getRandomName()
        print(self.name)
