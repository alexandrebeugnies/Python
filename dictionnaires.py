#coding:utf-8
"""
Création de dictionnaire: dico = {} #Vide
						  dico = {<cle>:<valeur>, <cle2>:<valeur>}
						  
Accès à une valeur : dico[<cle>]
Ajout et modification au dictionnaire : dico[<cle>] =<valeur>
Supression : dico.pop(<cle>)
			 del dico[<cle>]
"""
"""
dico = {"prénom":"Alexandre"}
print(dico["prénom"])
dico["chien"] = "C'est un mammifère, le meilleur ami de l'homme"
print(dico)
"""
dico = {"chat":"C'est un félin", "chien":"meilleur ami de l'homme"}
"""print(dico.has_key("chien"))"""
"""
dico.pop("chien")
print(dico)
"""
if "chien" in dico:
	print("Oui")
else:
	print("Non")

"""
valeur_supprimee = dico.pop("chien")
print(valeur_supprimee)
"""

for truc in dico.values():
	print(truc)
for key in dico.keys():
	print(key)
for k,v in dico.items():
	print("Clé : {} - Valeur : {}".format(k,v))

try:
	print(dico["OK"])
except KeyError:
	print("Cette valeur n'est pas une clé")
	
def maFonctionBizarre(**parametres):
	print(parametres)
	
maFonctionBizarre(p=154, nom="blablabla")
