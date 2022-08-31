#coding:utf-8

"""
Importer un  module : import <nom_module>
					  from <nom_module> import <nom_fonction>
					  from <nom_module> import *
"""

#import math -> adding math.sqrt()
"""from math import sqrt

resultat = sqrt(100)
print(resultat)

from math import sin
sinus = sin(42)
print(sinus)"""

import player
# import includes.player as player => includes.player.bye() => nom_dossier.nom_module
player.bye()
player.speak("Alex","Salut tout le monde :)")
