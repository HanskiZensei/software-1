numbers = []
number_input = (input("Enter a number: "))

while number_input != "":
    number = float(number_input)
    numbers.append(number)

    number_input = input("Enter a number: ")

numbers.sort(reverse=True)
five_numbers = numbers[:5]
print(f"The greatest numbers in descending order: ")
for num in five_numbers:
    print(num)
