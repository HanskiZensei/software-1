cabin_classes = {
    "LUX": "Upper-deck cabin with a balcony.",
    "A": "Above the car deck, equipped with a window.",
    "B": "Windowless cabin above the car deck.",
    "C": "Windowless cabin below the car deck.",
}
cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")
if cabin_class == "LUX":
    print(cabin_classes[cabin_class])
elif cabin_class == "A":
    print(cabin_classes[cabin_class])
elif cabin_class == "B":
    print(cabin_classes[cabin_class])
elif cabin_class == "C":
    print(cabin_classes[cabin_class])
else:
    print("Invalid cabin class.")
