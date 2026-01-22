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
