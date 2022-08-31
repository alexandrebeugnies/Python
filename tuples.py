#coding:utf-8

"""
!!! Conteneur immuable (dont on peut modifier les valeurs)
Création de tuple : mon_tuple = () #Vide
					mon_tuple = 17 #Une seule valeur
					mon_tuple = (17,) #idem qu'au-dessus
					mon_tuple = (4,6) #Plusieurs valeurs
					
2 raisons d'utiliser les tuples : affectation multiple de variable
								  retour multiple de fonction
"""
"""
mon_tuple = (45,64)

print(mon_tuple[0])

nombre1 = 14
nombre2 = 46
(nombre1, nombre2) = (14, 46)

print(nombre1)
print(nombre2)

nombre1 = 125
print(nombre1)
"""
def get_player_position():
	posX=148
	posY=86
	
	return(posX,posY)
#Programme principal
coordX = 0
coordY = 0
print("Position du joueur : ({}/{})".format(coordX, coordY))
coordX = 150
coordY = 150
print("Position du joueur : ({}/{})".format(coordX, coordY))
(coordX, coordY) = get_player_position()
print("Position du joueur : ({}/{})".format(coordX, coordY))
