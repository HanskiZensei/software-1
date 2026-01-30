import random


three_digits = ""
for i in range(3):
    digit = random.randint(0, 9)
    three_digits += str(digit)

four_digits = ""


for i in range(4):
    digit = random.randint(1, 6)
    four_digits += str(digit)

print("3-digit code:", three_digits)
print("4-digit code:", four_digits)
