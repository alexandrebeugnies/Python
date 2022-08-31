#coding:utf-8

import time

# 1er Janvier 1970 à 00h00
# time.sleep(nb en secondes)
# print(time.time())

"""
begin = time.time()
print("Début")

time.sleep(5)

end=time.time()
print("Fin")
print(f"Temps exécuté : {end - begin}s")
"""
"""
tps = time.localtime()
print(tps)

tps = time.mktime(tps)
print(tps)
"""
"""
%d : jour (01 à 31)
%m:  mois (01 à 12)
%Y: année - %y (00 à 99)
%H : heures (00 à 23)
%I : minutes (00 à 59)
%S : secondes (00 à 59)
%p : AM/PM
%A : jour/semaine / %a (jour abrégés)
%B: mois / %b (mois abrégé)
"""
my_time = time.strftime("%A")
print(my_time)

my_time = time.strftime("%d/%m/%Y")
print(my_time)
my_time = time.strftime("%Z")
print(my_time)
