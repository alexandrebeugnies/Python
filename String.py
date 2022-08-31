#coding:utf-8
"""
Une méthode de chaîne travaille sur une copie, et pas sur elle-même.

str.upper(),str.lower(), str.capitalize(), str.title(),
str.center(<largeur>, <caractere_remplissage>)

str.find(<chaine>, <debut>, <fin>)
str.index(<chaine>, <debut>, <fin>)
str.strip()
str.replace(<ancienne>, <nouvelle>, <occurences>)
str.isalpha() , str.isdigit(), str.isdecimal(), str.isnumeric(),str.isalphanum()
str.islower(), str.isupper() 
str.isidentifier(), str.iskeyword()
"""
# Classe str: string (chaines de caractères)
# help(str)

"""
ma_chaine = "Bonjour tout le monde !"

ma_chaine = ma_chaine.title()

print(ma_chaine)

ch1="bonjour"
ch2 = ch1
print(ch1)
print(ch2)
ch1 = ch1.upper()
print(ch1)
print(ch2)

machaine = "MonSuperProgramme"
print(machaine)

machaine = machaine.center(50, "_")
print(machaine)

chaine = "              MonSuperProgramme            "

print(chaine.find("Super"))
try:
	print(chaine.index("super"))
except ValueError:
	print("Je n'ai pas trouvé cette chaîne, essayez plutôt \"Super\"")
	
print(chaine)
print(chaine.strip())
"""

ma_chaine = "abracadabra"
print(ma_chaine)
ma_chaine = ma_chaine.replace("a", "z",2)

print(ma_chaine)

ma_chaine = ma_chaine.replace("a", "z")
print(ma_chaine)

phrase = "Magicien|10|5"

print(phrase.split("|"))

ch = "class"

if ch.isidentifier():
	print("Mot réservé")
else:
	print("Libre")
	
ch = "Le langage Python"

if "langage" in ch:
	print("Trouvé")
else:
	print("Non trouvé")
