'''
print ("Hello World")
print ("Hei,sanoi \nVille")
print ("Hyvää")
print ("huomenta")
käyttäjä = input("Anna nimesi: ")
ikä=input ("Anna ikäsi:")
print(f"Hei, sanoi:\n\t{käyttäjä} ikä:{ikä}")
'''

# luku1 = float(input("Anna luku:"))
# luku2 = float(input("Anna luku:"))
# tulo = luku1 * luku2
# print(f"lukujen {luku1} ja {luku2} tulo on {tulo}")

# pisteet = 50  # Muuttujan pisteet arvo on nyt 50
# print(pisteet)  # Tulostaa: 50
#
# pisteet = 120  # Nyt muuttujan pisteet arvo on 120
# print(pisteet)  # Tulostaa: 120

# muuttuja = "tekstiä" #merkkijono eli string
# print(muuttuja)
# luku = 123 #kokonaisluku eli int
# print(luku)
# liukuluku= 3.2 #liukuluku eli float
# print (liukuluku)
# totuusarvo = true totuusarvo eli boolean
# print (totuusarvo)

#import random

#three_digits = ""
#four_digits = ""
#for i in range(3):
#    digit = random.randint(0,9)
#   three_digits += str(digit)

#for i in range(4):
#    four_digits += str(digit)
#    digit = random.randint(1,6)

#print("3-digit code:", three_digits)

# komento = input("Anna komento: ")
# while komento != "lopeta" and komento != "Lopeta":
#     print("Suoritan toiminnon: " + komento)
#     komento = input("Anna komento: ")
# print("Toiminnot lopetettu.")
# import random
#
# noppa1 = noppa2 = heitot = 0 #nollataan kaikki 3 muuttujaa
# while (noppa1 != 6 or noppa2 != 6):
#         noppa1 = random.randint(1, 6)
#         noppa2 = random.randint(1, 6)
#         heitot += 1
#         print(f"Heitit nopat {noppa1}, {noppa2}")
# print(f"Tarvittiin {heitot} heittoa.")
# eka = 1
# while eka <= 5:
#     toka = 1
#     while toka <=5:
#         print(f"{eka} kertaa {toka} on {eka*toka}")
#         toka = toka + 1
#     eka = eka + 1
#  import random
#  toistot = 0
#  heitot_yhteensä = 0
#  while toistot < 100000:
#
#      noppa1 = noppa2 = heitot = 0
#      while (noppa1!=6 or noppa2!=6):
#          noppa1 = random.randint(1,6)
#         noppa2 = random.randint(1,6)
#         heitot = heitot + 1
#     print(f"Tarvittiin {heitot} heittoa.")
#     toistot = toistot + 1
#     heitot_yhteensä = heitot_yhteensä + heitot
#
# heitot_keskimäärin = heitot_yhteensä/toistot
# print(f"Heitot keskimäärin: {heitot_keskimäärin:6.2f}")

# tämä ei toimi koska rolls on määritettävä ennen while looppia
# import random
#
#
# def roll_dice ():
#     noppa = random.randint (1, 6)
#     print(noppa)
#     return noppa
#
#
# roll = 1


# while roll != 6:
#     roll = roll_dice()
# halkasija2 = input("Enter the diameter of the second pizza (cm): ")
# hinta2 = input("Enter the price of the second pizza (euros): ")
# Use a dictionary to store ICAO: Airport Name pairs
# airports = {}
#
#
# def get_choice():
#     print("\nAirport Data Management")
#     print("1. Enter a new airport")
#     print("2. Fetch airport information")
#     print("3. Quit")
#     choice = input("Please choose an option (1-3): ")
#     return choice
#
#
# # Main Program Loop
# while True:
#     user_input = get_choice()
#
#     if user_input == "1":
#         icao = input("Enter the ICAO code: ").upper()
#         name = input("Enter the airport name: ")
#         airports[icao] = name
#         print(f"Airport {name} with ICAO code {icao} has been added.")
#
#     elif user_input == "2":
#         icao = input("Enter the ICAO code: ").upper()
#         if icao in airports:
#             print(f"The airport with ICAO code {icao} is {airports[icao]}.")
#         else:
#             print("ICAO code not found.")
#
#     elif user_input == "3":
#         print("Thank you for using the Airport Data Management system. Goodbye!")
#         break  # This exits the loop and the program
#
#     else:
#         print("Invalid choice, please select 1, 2, or 3.")


def saldo_on(saldo_nyt):
    on_matkoja = saldo_nyt >= 170
    return on_matkoja


def matkusta(saldo_nyt, hinta):
    saldo_nyt = saldo_nyt - hinta
    return saldo_nyt


saldo_euroissa = float(input("Lataa alkusaldo: "))
saldo = int(saldo_euroissa * 100)

while saldo_on(saldo):
    matkatyyppi = int(input("Minkä matkan haluat leimata? 1) aikuinen 2) lapsi: "))
    if matkatyyppi == 1:
        matkan_hinta = 330
    elif matkatyyppi == 2:
        matkan_hinta = 170
    else:
        print("Syötä 1 tai 2 ")
        matkan_hinta = 0
    saldo = matkusta(saldo, matkan_hinta)
    print(f"Matkustit ja saldoa on jäljellä {saldo/100:.2f} euroa. ")

print(f"Saldosi loppui, et voi enää matkustaa. Saldoa jäi {saldo/100:.2f} euroa. ")