#coding:utf-8

"""
Nommer une variable: doit commencer par une lettre ou underscore
					 ne pas contenir d'espaces
					 ne pas contenir de caractères spéciaux
					 utiliser des underscores(_)
					 
exemples: agePersonne
		  age_personne
		  AgePersonne
		  agepersonne
		  Age_Personne
		  _AgePersonne
          _age_persone
          
Types standards: entier (int)
				 nombres flottants(float)
				 chaine de caractères(str)
				 booléen(bool)
				 autres(listes,dictionnaires,tuple,etc.)

Fonctions vues : print() -> afficher à l'écran
				 input() -> lire au clavier
				 type() -> retourne le type d'une donnée, d'une variable,etc.
				 int(), float(),str(), bool()=> caster une donnée
				 str.format() -> formater une chaine 
"""

agePersonne = 14
prixHT= 120.46
agePersonne2 = "25"
continuer_partie = True

print(type(agePersonne))
print(type(agePersonne2))
 
print("âge de la personne:",agePersonne)

texte = "l'âge de la personne est {} et le prix HT est de {} euros"
print(texte.format(agePersonne, prixHT))
print("l'âge de la personne est {} et le prix HT est de {} euros".format(agePersonne, prixHT))

nomJoueur = input("Entrer un nom de joueur :")
print("Bienvenue,", nomJoueur)

prixHT = input("Entrer un prix Hors TVA :")
prixHT = int(prixHT)
prixTTC = prixHT + (prixHT * 20 /100)

print("Prix TTC =", prixTTC)

valeur_booleen = False
valeur_booleen = int(valeur_booleen)

print(valeur_booleen)


