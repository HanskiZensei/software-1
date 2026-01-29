import random


def roll_dice(sides):
    noppa = random.randint(1, sides)
    print(noppa)
    return noppa


sideinput = int(input("Enter how many sides for the dice: "))


while True:
    roll = roll_dice(sideinput)

    if roll == sideinput:
        break
