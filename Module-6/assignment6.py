def kysely(halkasija, hinta):
    for i in range(halkasija, hinta):
        print(halkasija + "" + str(i+1) + "pizza")
    return


kysely(f"{halkasija}", 2)
halkasija = input("Enter the diameter of the first pizza (cm): ")
hinta = input("Enter the price of the first pizza (euros): ")
