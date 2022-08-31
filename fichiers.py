#coding:utf-8

"""
Mode d'ouverture : r (lecture seule)
				   w (écriture avec remplacement)
				   a (écriture avec ajout en fin de fichier)
				   x (lecture et écriture)
				   r+ (lecture/écriture dans un même fichier)
				   
Lecture : read(), readline(), readlines() -> recupère des strings (caster si on a besoin de faire des opérations)

"""
"""
fic = open("donnees.txt", "r")
content = fic.read()
print(content)

line = fic.readline()
print(line)

line = fic.readline()
print(line)

line = fic.readline()
print(line)

line = fic.readlines()
print(line)
fic.close()
if fic.closed:
	print("Fichier fermé")
else:
	print("Fichier encore ouvert")
"""
"""
with open("donnees.txt", "r") as fic:
	content = fic.read()
	print(content)
	# Dans ce cas, il n'est pas nécessaire de fermer le fichier
"""
"""
with open("donnees.txt", "w") as fic:
	nombre = 15
	fic.write(str(nombre))
	fic.write("\tBonjour, je suis une phrase\n")
	fic.write("Je suis une autre phrase\n")
"""
import pickle
class Player:
	def __init__(self, name, level):
		self.name = name
		self.level = level
	def whoami(self):
		print("{} ({})".format(self.name,self.level))


"""
p1 = Player("Alexandre", 20)
p1.whoami()
"""
with open("player.data","rb") as fic:
	"""
	record = pickle.Pickler(fic)
	record.dump(p1)
	"""
	get_record = pickle.Unpickler(fic)
	player_one = get_record.load()
player_one.whoami()
