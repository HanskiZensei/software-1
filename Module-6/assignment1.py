import random


def roll_dice():
    noppa = random.randint(1, 6)
    print(noppa)
    return noppa


roll = 1


while roll != 6:
    roll = roll_dice()
