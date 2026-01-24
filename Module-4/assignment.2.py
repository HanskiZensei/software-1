inches = input("Enter length in inches: ")
if inches >0:
    centimeters = inches*2.54
    print(f"{inches:.2f} inches is {centimeters:.2f} centimeters")
else:
    print("Program ended.")