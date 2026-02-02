import math

halkasija = float(input("Enter the diameter of the first pizza (cm): "))
hinta = float(input("Enter the price of the first pizza (euros): "))

halkasija2 = float(input("Enter the diameter of the second pizza (cm): "))
hinta2 = float(input("Enter the price of the second pizza (euros): "))


def calculate_unit_price(halkasija, hinta):
    radius = halkasija / 2
    square_cm = math.pi * radius ** 2
    square_meter = square_cm / 10000
    price_per_square_meter = hinta / square_meter
    return price_per_square_meter


loppuhinta = calculate_unit_price(halkasija, hinta)
loppuhinta2 = calculate_unit_price(halkasija2, hinta2)

print(f"Unit price of the first pizza: {loppuhinta:.2f} euros/m²")
print(f"Unit price of the second pizza: {loppuhinta2:.2f} euros/m²")


if loppuhinta < loppuhinta2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")

