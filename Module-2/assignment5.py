talents=float(input("Enter talents: "))
pounds=float(input("Enter pounds: "))
lots=float(input("Enter lots: "))

talents_in_pounds=float(talents*(20*32*13.3))
pounds_in_lots=float(pounds*(32*13.3))
lots_in_grams=float(lots*13.3)

total_grams=float(talents_in_pounds+pounds_in_lots+lots_in_grams)
kilograms=int(total_grams//1000)
remaining_grams= round(float(total_grams % 1000),2)

print ("The weight in modern units:")
print (f"{kilograms} kilograms and {remaining_grams:.2f} grams.")
