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
import random

# 3-digit code (0–9)
code3 = ""
for i in range(3):
    code3 += str(random.randint(0, 9))

# 4-digit code (1–6)
code4 = ""
for i in range(4):
    code4 += str(random.randint(1, 6))

print("3-digit code:", code3)
print("4-digit code:", code4)

#import random

#three_digits = ""

#for i in range(3):
#    digit = random.randint(0,9)
 #   three_digits += str(digit)

#print("3-digit code:"), three_digits



