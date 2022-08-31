#coding:utf-8

"""
Propriété : manière de manipuler/contrôler des attributs
			Principe d'encapsulation
"""

class Humain:
	"""
	Cette classe représente un Humain
	"""
	def __init__(self, nom, age):
		print("Création d'un Humain ...")
		self.nom = nom
		self._age = age
		
	def	_getage(self):
		#print("Récupération interdite")
		try:
			return self._age
		except AttributeError:
			print("L'âge n'existe pas !")
			
		
		
	def _setage(self,nouvel_age):
		if nouvel_age < 0 :
			self._age = 0
		else:
			self._age = nouvel_age
	
	def _delage(self):
		del self._age
		
	# property(<getter>, <setter>, <delete>, <helper>)
	age = property(_getage, _setage, _delage,"Je suis l'age d'un Humain")
		
# Programme Principal 
h1 = Humain("Alexandre",26)

print(h1.age)

del h1.age
print(h1.age)

help(Humain.age)


