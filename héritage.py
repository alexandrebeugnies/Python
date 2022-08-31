#coding:utf-8

#Classe Mère
class Vehicule:
	
	def __init__(self, nom, quantite_essence):
		self.nom = nom
		self.essence = quantite_essence
	def se_deplacer(self):
		print("Le véhicule {} se déplace ... ".format(self.nom))

# Classe Fille		
class Voiture(Vehicule):
	def __init__(self, nom_voiture, essence, puissance):
		Vehicule.__init__(self,nom_voiture, essence)
		self.puissance = puissance
	def se_deplacer(self):
		print("je roule ...")

class Avion(Vehicule):
	def __init__(self, nom, essence, marchandise):
		Vehicule.__init__(self, nom , essence)
		self.marchandise = marchandise
	def se_deplacer(self):
		print("je survole les airs !")
#Programme Principal
"""
v1 = Vehicule("F22 Raptor",2400)
v2 = Vehicule("Toyota Supra",90)
print(v1.nom)
print(v2.nom)
v1.se_deplacer()
"""
voiture1 = Voiture("Toyota Supra",90,420)
voiture1.se_deplacer()
print(voiture1.puissance, "CH")

av1 =Avion("F22 Raptor",2400,"Missiles")
av1.se_deplacer()
