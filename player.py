#coding:utf-8

"""
Module pour le joueur
"""

def speak(personnage,message):
	print("{} : {}".format(personnage,message))
	
def bye():
	print("Au revoir ! :)")
	
	
if __name__ == "__main__":
	speak("Alex","Bonjour tout le monde ! :)")
	bye()
