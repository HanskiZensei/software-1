integer = int(input("Enter an integer: "))

prime = True

if integer <= 1:
    prime = False
else:
    for i in range (2, integer):
        if integer % i == 0:
            prime = False

if prime:
    print(f"{integer} is a prime number. ")
else:
    print(f"{integer} is not a prime number. ")
