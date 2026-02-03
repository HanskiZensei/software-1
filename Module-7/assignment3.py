icao_airport = []


def check(user_input):
    user_choices = {
        "Enter ICAO code and the name of the airport": (1),
        "Enter ICAO code and the name of the airport": (2),
        "Thank you for using the Airport Data Management system. Goodbye!": (3),
    }
    for choice in user_choices.items():
        if user_input in user_choices:
            return choice


user_input = int(input("Please choose an option (1-3): "))


if user_input < 1 or user_input > 3:
    print("Please enter (1-3): ")
