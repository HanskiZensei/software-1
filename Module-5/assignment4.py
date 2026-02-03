kaupungit = []


for i in range(5):
    kaupunki = input("Enter the name of a city: ")
    kaupungit.append(kaupunki)


valmislista = kaupungit
print()
print("\nThe cities you entered: ")
for lista in valmislista:
    print(lista)
