#coding:utf-8

class Animal:
	def __init__(self, nom):
		self.nom = nom
	def manger(self):
		print(self.nom, "mange...")
		
class Reptile(Animal):
	def __init__(self, nom, regime_alimentaire):
		Animal.__init__(self, nom)
		self.regime = regime_alimentaire
	def manger(self):
		print("Le reptile mange ...")	
		
#Code Principal
lezard = Reptile("Lézard", "Grenouilles")
if isinstance(lezard,Animal):
	print("Lézard est un Animal")		
#lezard.manger()
if issubclass(Reptile,Animal):
	print("Reptile hérite d'Animal")
