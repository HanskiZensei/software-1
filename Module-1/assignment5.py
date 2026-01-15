talents=int(input("Enter talents: "))
pounds=int(input("Enter pounds: "))
lots=int(input("Enter lots: "))
talents_in_pounds=20*32*13.3*talents
pounds_in_lots=32*13.3*pounds
lots_in_grams=13.3*lots
total_grams=talents_in_pounds+pounds_in_lots+lots_in_grams
kilograms=total_grams//1000
remaining_grams=total_grams%kilograms
print(f"The weight in modern units:\n{kilograms} kilograms and {remaining_grams} grams.")
