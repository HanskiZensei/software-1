length_of_the_zander = float(input("Enter the length of the zander in centimeters: "))

if  length_of_the_zander < 42:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {42 - length_of_the_zander:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")