import random
dice_count = int(input("How many dice to roll: "))
dice_rolls = []

for i in range(dice_count):
    dice = random.randint(1, 6)
    print(f"Heitit {dice}")
    dice_rolls.append(dice)

print(f"Sum of the dice: {sum(dice_rolls)}")



