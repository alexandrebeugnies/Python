#coding:utf-8


class Humain:
	"""Classe des êtres humains """
	
	humains_crees = 0
	
	def __init__(self, c_prenom, c_age):
		print("Création d'un Humain ...")
		self.prenom = c_prenom
		self.age = c_age
		Humain.humains_crees += 1
		
		

print("Lancement du programme ....")

h1 = Humain("Jojo",34)
print("Prénom de h1 : {}".format(h1.prenom))
print("Age de h1 : {}".format(h1.age))
print("Humains Existants : {}".format(Humain.humains_crees))
# print("Prénom de h1 -> {}".format(h1.prenom))
h2 = Humain("Albert",14)
print("Prénom de h2 : {}".format(h2.prenom))
print("Age de h2 : {}".format(h2.age))
# self --> affiche l'adresse de l'objet.
print("Humains Existants : {}".format(Humain.humains_crees))
