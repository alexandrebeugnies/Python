#coding:utf-8

# Création d'une liste
import copy
# Ne fais pas de copie -> liste2 = liste1
liste1 = ["arc","bouclier","épée"]
liste2 = copy.deepcopy(liste1)

print("Liste 1",liste1[:])
print("Liste 2",liste2[:])

liste2.append("potion")
print("Liste 1",liste1[:])
print("Liste 2",liste2[:])

liste2 = ["Parchemin","Carte"]
print(liste1[:])
"""liste1.extend(liste2)
print(liste1[:])"""
liste1 += liste2
print(liste1[:])
"""
inventaire = ["Bonjour","à","tous"]
phrase = "_".join(inventaire)
print(phrase)
"""
"""
inventaire = [0] * 10 # Multiplie le nombre d'occurences d'un élément
inventory = range(20)

i=0
"""
"""
while i < len(inventory):
	print(inventory[i])
	i += 1
"""
#inventory = ["Arc","épée", "bouclier","potion","flèches","tunique"]
"""
inventaire= ["Potion de Mana","Arc","Bouclier","Manteau de Cuir","Arbalète","Potion de Mana"]
print(inventaire[:])

inventaire.sort()
print(inventaire[:])

inventaire.reverse()
print(inventaire[:])

print("Nombre de Potions : ", inventaire.count("Potion de Mana"))

inventaire.clear()
print(inventaire[:])
"""
"""
objet_a_supprimer = inventaire.index("Bouclier")
del inventaire[objet_a_supprimer]
print(inventaire[:])
"""


"""
inventaire.remove("Bouclier")
print(inventaire[:])

del inventaire[1]
print(inventaire[:])
"""
"""inventaire.append("Arc")
print(inventaire[:])

inventaire.append("Bouclier")
print(inventaire[:])

inventaire.insert(1,"Potion de Mana")
print(inventaire[:])"""
"""if "bouclier" in inventory:
	print("Je possède un bouclier")
else:
	print("Je ne possède pas de bouclier")
"""
"""
print(inventory[:])

inventory[:] = ["Bouclier d'acier"] * len(inventory)
print(inventory[:])

inventory[2:4] = ["bouclier d'acier"] * 2
print(inventory[:])

inventory[4] = "manteau"
print(inventory[:])
"""
"""
for valeur in inventory:
	print(valeur)
	
print(inventory[:])
print(inventory[:2])
print(inventory[2:])
print(inventory[-3])
print(inventory[2:4])
"""

#print(inventaire)
#print(inventory)
#[:] affiche toute la liste
#[:2] affiche les premiers éléments sans afficher le troisième
#[2:] affiche les derniers éléments
#[-3] affiche le troisième éléments en partant du sens inverse de la liste
# liste[A:B] = Affiche de l'élément d'indice A à l'élément d'indice B (exclus) => B-A = nombre d'élements affichés

inventaire = ["arc","bouclier","épée"]
for indice_objet, valeur_objet in enumerate(inventaire):
	print("Element d'indice {} -> {}".format(indice_objet, valeur_objet))
