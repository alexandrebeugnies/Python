#coding:utf-8

"""
Opératuers de comparaison : == (égal à)
							!= (différent de)
							< (plus petit que)
							> (plus grand que)
							<= (plus petit ou égal)
							>= (plus grand ou égal)
							
Conditions multiples : and (ET)
					   or (OU)
					   in/not in (DANS / PAS DANS)
"""

identifiant = "Alexandre"
mot_de_passe = "password123"

print("Interface de connexion")

user_id = input("Entrez votre identifiant :\n")
user_password = input("Entrez votre mot de passe :\n")

if user_id == identifiant and user_password == mot_de_passe :
	print("Vous êtes connectés, bienvenue", user_id)
else:
	print("Erreur combinaison identifiant / mot de passe")

lettre_hasard= "b"

if lettre_hasard not in "aeiouy":
	print("C'est une consonne ")
else:
	print("c'est une voyelle")
"""if lettre_hasard  in "aeiouy":
	print("C'est une voyelle ")"""

age = 24

if age == 18:
	print("Tu viens d'être majeur")
elif age == 50:
	print("Tu viens d'avoir 50 ans")
elif age == 60:
	print("Tu viens d'avoir 60 ans")
else: 
	print("Tu as",age,'ans')
	
age1 = input("Quel age as tu ?\n")
age1=int(age)

if age>0 and age<=100:## age>0>=100
	print("l'age est validé")
else:
	print("l'age est incorrect")
