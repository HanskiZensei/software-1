integer = input("Enter an integer: ")
if (integer % 1 == 0) and (integer % integer == 0):
    print(f"Integer is a prime number.")
elif (integer % 1 == 0) and (integer % 0, 10 == 0):
    print(f"Integer is not a prime number.")