names = set()


while True:
    name = input("Enter names: ")
    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nAll entered names: ")
for n in names:
    print(n)
