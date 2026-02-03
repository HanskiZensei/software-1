def get_season(month):
    seasons = {
        "winter": (12, 1, 2),
        "spring": (3, 4, 5),
        "summer": (6, 7, 8),
        "autumn": (9, 10, 11),
    }
    for season, months in seasons.items():
        if month in months:
            return season


month = int(input("Enter the number of a month (1-12): "))


if month < 1 or month > 12:
    print(f"You entered: {month}")
    print("Please enter a number between 1 and 12. ")


else:
    month_name = get_season(month)
    print(f"You entered: {month} ")
    print(f"The season is {month_name}. ")
