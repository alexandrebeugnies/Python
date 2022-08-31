#coding:utf-8
import sqlite3
from unittest import result

try:
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    req = cursor.execute('SELECT * FROM tt_users')
    
    for row in req.fetchall():
        print(row[1])
except Exception as e:
    print("[ERREUR]",e)
    connection.rollback()
finally:
    connection.close()


#print(type(connection))
#print(type(cursor))

"""
my_username=("Alexandre",)

cursor.execute('SELECT * FROM tt_users WHERE user_name = ?', my_username)
result = cursor.fetchone()[1]

print(f"Le nom d'utilisateur est : {result}")
"""
"""
new_user = (cursor.lastrowid, "Jason", 12 )
cursor.execute('INSERT INTO tt_users VALUES (?,?,?)', new_user)
connection.commit()
print("Nouvel Utilisateur ajouté !")
"""


#print(req.fetchall())


#connection.rollback()

