#coding:utf-8

"""compteur = 0


while compteur < 5:
	print("Je suis une phrase")
	compteur += 1"""
	
jeu_lance = True

while jeu_lance:
	#Fais des instructions en rapport avec le jeu
	choixMenu = input("> ")
	
	if choixMenu == "again":
		continue
	elif choixMenu == "quit":
		jeu_lance = False
	elif choixMenu == "hello":
		print("Bonjour :) !")
	else:
		print("Commande introuvable")
		
print("A bientôt")

"""
Boucles: while / for
Keyword: break (casse la boucle) / continue (revient au début de la boucle)
"""

sentence = "Bonjour tout le monde"
 
for letter in sentence:
	 print(letter)

