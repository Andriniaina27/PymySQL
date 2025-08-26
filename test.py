from mysql.connector import connect, Error
import pymysql

print("Début test connexion MySQL")

try:
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="voyage",
        port=3306
    )
    print("Connexion réussie")
    db.close()
except Error as e:
    print("Erreur de connexion :", e)
    
input("Appuyez sur Entrée pour fermer…")