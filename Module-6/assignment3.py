def gallons_to_liters(gallon_count):
    liters = gallon_count * 3.785
    print(f"{gallon_count} American gallons is {liters:.2f} liters. ")


while True:
    gallon_count = float(input("Enter a volume in American gallons (negative value to quit): "))
    if gallon_count < 0:
        print("Program finished. ")
        break
    gallons_to_liters(gallon_count)
