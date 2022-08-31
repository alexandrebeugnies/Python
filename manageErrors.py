#coding:utf-8

"""
Gérer les exceptions : try, except (+ else, finally)

Types d'exceptions : ValueError
					 NameError
					 TypeError
					 ZeroDivisionError
					 OSError
					 AssertionError
					 
"""

ageUtilisateur = input("Quel âge as-tu ?\n")
try:
	ageUtilisateur = int(ageUtilisateur)
except:
	print("L'âge indiqué n'est pas correcte !!")
else:
	print("Tu as",ageUtilisateur, "ans") 
finally:
	print("FIN DU PROGRAMME ...")

# finally est toujours exécuter quoi qu'il advienne

nombre1 = 150
nombre2 = input("Choisir le nombre pour le diviser : ")
try:
	nombre2 = int(nombre2)
	print("Résultat = {}".format(nombre1/nombre2))
except ZeroDivisionError:
	print("Vous ne pouvez pas diviser par 0.")
except ValueError:
	print("Vous devez entrer un nombre")
except:
	print("Valeur incorrecte")
else:
	print("Bravo, tu as noté un nombre valide !!!")
finally:
	print("Fin du programme ...")


try:
		age = input("Quel âge as-tu ?")
		age= int(age)
		if age < 25:
			raise ZeroDivisionError("Coucou")
except ZeroDivisionError:
	print("J'ai attrapé ton exception inutile")


try:
	age = input("Quel âge as-tu ?")
	age= int(age)
	assert age < 25 # Je veux que age soit supérieur à 25
except AssertionError:
	print("J'ai attrapé l'exception")



	



