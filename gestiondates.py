#coding:utf-8
import datetime
from datetime import date
"""d1 = datetime.datetime(2022, 8, 23, 15, 10, 0)
print(d1)
d2 = datetime.datetime(2022, 8, 22, 15, 10, 0)
print(d2)
"""
"""
if d1 < d2:
	print("d1 est plus ancien que d2")
else:
	print("d1 est plus récent que d2")"""

#print(d1.year)

"""t1 = datetime.time(23, 6, 00)
print(t1)"""
now=date.today()
print(now)
born = datetime.date(1996, 1, 10)
print(f"{now.year - born.year} ans.")
