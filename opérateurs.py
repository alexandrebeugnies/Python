#coding:utf-8

"""
Opérateurs en Python : + (addition)
					   - (soustraction)
					   * (multiplication)
					   / (division)
					   % (modulo) -> reste de la division Euclidienne
"""

"""calcul = 5 / 2
calcul = float(calcul)
calcul2 = 5 % 2
calcul2 = int(calcul2)
print("Résultat =", calcul)
print("le reste est de :", calcul2)

calcul3 = 5 + 3 * 7

print(calcul3)"""

niveauPersonnage = input("Niveau de départ ?\n")
niveauPersonnage = int(niveauPersonnage)
print("Niveau du personnage", niveauPersonnage)

print("Combat réussi, tu gagnes un niveau !")
niveauPersonnage += 1 

print("Niveau du personnage", niveauPersonnage)
