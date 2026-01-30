import random


random_number = random.randint (1, 10)
user_guess = int(input("Guess a number between 1 and 10: "))


while user_guess != random_number:
    if user_guess > random_number:
        print("Too high")
    else:
        print("Too low")
    user_guess = int(input("Guess a number between 1 and 10: "))

print("Correct")
