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








from Models.model import Base
class Group:
    __base = Base() #class
    def __init__(self, code):
        self.base = Base() #objet
        self.code = code
        self.nomG = None

        self.base.cur.execute("SELECT NomG FROM groupe WHERE Code = %s", (self.code,))
        dico = self.base.cur.fetchone()

        if dico:
            self.nomG = dico["NomG"]

    def __str__(self):
        chaine = f"Code: {self.code}\n Nom: {self.nomG}\n"
        return chaine

    @classmethod
    def get_all(cls):
        cls.__base.cur.execute("SELECT * FROM groupe")
        return cls.__base.cur.fetchall()

    @classmethod
    def get_by_id(cls, id):
            cls.__base.cur.execute("SELECT * FROM groupe WHERE Code = %s", (id,))
            return cls.__base.cur.fetchone()

    @classmethod
    def insert(cls, nom):
        cls.__base.cur.execute("INSERT INTO groupe VALUES (NULL, %s)", (nom,))
        cls.__base.con.commit()

    @classmethod
    def update(cls, id, nom):
        cls.__base.cur.execute("UPDATE groupe SET NomG = %s WHERE Code = %s", (nom, id))
        cls.__base.con.commit()

    @classmethod
    def delete(cls, id):
        cls.__base.cur.execute("DELETE FROM groupe WHERE Code = %s", (id,))
        cls.__base.con.commit()





// touriste

from Models.model import Base

class Tourist:
    __base = Base()
    def __init__(self, id, base: Base):
        self.base = base
        self.numero = id
        self.nom = None
        self.codeG = None

        self.base.cur.execute("SELECT Nom, CodeG FROM touriste WHERE Numero = ?", (self.numero,))
        dico = self.base.cur.fetchone()

        if dico:
            self.nom = dico["Nom"]
            self.codeG = dico["CodeG"]

    def __str__(self):
        chaine = f"Numero: {self.numero}\nNom: {self.nom}\nGroup {self.codeG}"
        return chaine

    @classmethod
    def get_all(cls):
        cls.__base.cur.execute("SELECT * FROM touriste")
        return cls.__base.cur.fetchall()

    @classmethod
    def get_by_id(cls, id):
        cls.__base.cur.execute("SELECT * FROM touriste WHERE Numero = ?", (id,))
        return cls.__base.cur.fetchone()

    @classmethod
    def insert(cls, nom, group_code):
        cls.__base.cur.execute("INSERT INTO touriste VALUES (%s, %s)", (nom, group_code))
        cls.__base.con.commit()

    @classmethod
    def update(cls, id, nom, group_code):
        cls.__base.cur.execute("UPDATE touriste SET Nom = %s, CodeG = %s WHERE Numero = %s", (nom, group_code, id))
        cls.__base.con.commit()

    @classmethod
    def delete(cls, id):
        cls.__base.cur.execute("DELETE FROM touriste WHERE Numero = %s", (id,))
        cls.__base.con.commit()



main.py


from Models.model import Base
from Models.Tourist import Tourist
from Models.Group import Group

base = Base()

tourist_6 = Tourist(6, base)
tourist_7 = Tourist(7, base)
tourist_8 = Tourist(8, base)
tourist_9 = Tourist(9, base)

groupes = Group.all_instances()
for group in groupes:
    print("-----------------------------------------------------")
    print("Membres de la groupe: ", group.get_nom())
    print("-----------------------------------------------------")
    membersOfGroup =  group.get_members()
    for member in membersOfGroup:
        print(member.get_nom())


base.close()