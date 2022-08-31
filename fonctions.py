#coding:utf-8

"""
Fonctions vues: print(), input()
				type(), int(), float(), str(), bool()
"""



age = input("Quel ages as tu?\n")
age=int(age)

print("Tu as {} ans".format(age))

def dire_bonjour():
	print("Bonjour à tous ! :)")
	
# Je ne suis plus dans la fonction
dire_bonjour()

def dire(nom_personne = "Tom",age_personne=18,message_personne="Salut !"):
	print("{} ({} ans) : {}".format(nom_personne,age_personne,message_personne))

dire("Jason")
dire("Tom")
dire(message_personne = "Yo !" , age_personne = 25, nom_personne = "Roger" )

def show_inventory(*list_items):
	for item in list_items:
		print(item)
	
show_inventory("épée")
show_inventory("épée","arc","potion de mana","cape de Dragon Rouge")

def calculer_somme(nombre1,nombre2):
	"""resultat = nombre1 + nombre2
	return resultat"""
	return  nombre1 + nombre2

print(calculer_somme(5,16))
	
def comparer_nombres(nombre1,nombre2):
	if nombre1 > nombre2:
		return nombre1
	elif nombre1 < nombre2:
		return nombre2
	else:
		return "Egalité"
	
print(comparer_nombres(230,260))

print("1. Faire une somme")
print("2. Faire une différence")
print("3. Faire une multiplication")
print("4. Quitter le programme")

coucou = lambda:print("Bonjour")

coucou()

ttc = lambda prixHT:prixHT + (prixHT * 20 / 100)
print(ttc(24))

calculer = lambda a,b : a + b
print(calculer(14,27))
