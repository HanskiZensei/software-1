airports = {}


def choice():
    print("\nAirport Data Management ")
    print("1. Enter a new airport ")
    print("2. Fetch airport information ")
    print("3. Quit")
    user_choice = input("Please choose an option (1-3): ")
    return user_choice


while True:
    user_choice = choice()
    if user_choice == "1":
        icao = input("Enter the ICAO code: ").upper()
        airport = input("Enter the airport name: ")
        airports[icao] = airport
        print(f"Airport {airport} with ICAO code {icao} has been added. ")

    elif user_choice == "2":
        icao = input("Enter the ICAO code: ").upper()
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}. ")
        else:
            print(f"No airport found with ICAO code {icao}. ")


    elif user_choice == "3":
        print("Thank you for using the Airport Data Management system. Goodbye! ")
        break
    else:
        print("Invalid option please choose 1, 2 or 3. ")