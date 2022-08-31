#coding:utf-8

"""
Méthodes : fonction sur une instance(objet)
Méthode de classe: fonction sur une classe
Méthode statique: fonction indépendante mais "liée" à une classe
"""

class Humain:
	"""Classe qui définit un humain"""
	lieu_habitation = "Terre"
	
	def __init__(self, nom, age):
		self.nom = nom
		self.age = age
	def parler(self,message): # self= méthode standard
		print("{} a dit : {}".format(self.nom,message))
	def changer_planete(cls,nouvelle_planete): #cls = méthode de classe
		Humain.lieu_habitation = nouvelle_planete
		
	changer_planete = classmethod(changer_planete)
	
	def definition():
		print("L'humain est classé comme étant le plus haut être vivant de la chaine alimentaire")
	definition = staticmethod(definition)
#Programme Principal
h1 = Humain("Alex",26)

h1.parler("Bonjour tout le monde :)")
h1.parler("ça va :)")

print("Planète actuelle : {}".format(Humain.lieu_habitation))
Humain.changer_planete("Mars")
print("Planète actuelle : {}".format(Humain.lieu_habitation))
Humain.definition()
