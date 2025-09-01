from .model import Model

class Touriste(Model):
    def __init__(self, id):
        # self.db = Database()
        self.numero = id
        # self.base = base
        self.nom = None
        self.id_groupe = None

        dico = Touriste.getById(id)
        # self.base.cursor.execute("SELECT nom, groupe_id FROM touriste WHERE id = ?", (self.numero,))
        # dico = self.base.cursor.fetchone()
        print(dico)
    
    def all(self):
        get = Touriste.getAll() 
        for x in get:
            print(x)

    def somme(self):
        somme = Touriste.count()
        print(somme)
        # self.nom = dico["nom"]  
        # self.id_groupe = dico["groupe_id"]

    # @classmethod
    # def getAll(cls):
    #     cls.__base.cursor.execute("SELECT * FROM touriste")
    #     return cls.__base.cursor.fetchall()
    
    # @classmethod
    # def getById(cls, numero):
    #     cls.__base.cursor.execute("SELECT * FROM touriste WHERE id = ?",(numero,))
    #     return cls.__base.cursor.fetchone()
    
    # @classmethod
    # def insert(cls, nom, prenom, age, groupe_id):
    #     cls.__base.cursor.execute("INSERT INTO touriste VALUES(NULL, %s, %s, %s, %s)", (nom, prenom, age, groupe_id))
    #     cls.__base.connexion.commit()

    # @classmethod
    # def update(cls, nom, prenom, age, groupe_id, id):
    #     cls.__base.cursor.execute("UPDATE touriste SET nom = %s, prenom = %s, age = %s, groupe_id = %s WHERE id = %s",(nom, prenom, age, groupe_id, id))
    #     cls.__base.connexion.commit()
    
    # @classmethod
    # def delete(cls, id):
    #     cls.__base.cursor.execute("DELETE FROM touriste WHERE id = %s", (id,))
    #     cls.__base.connexion.commit()
    
        

    # def ajoutTouriste(self, nom, prenom, age, groupe_id):
    #     requete = "INSERT INTO touriste VALUES(NULL, %s, %s, %s, %s)"
    #     self.db.execute(requete, nom, prenom, age, groupe_id)
    #     print("Touriste ajouté avec succès !")
    
    # def supprimerTouriste(self, id):
    #     req = "DELETE FROM touriste WHERE id = %s"
    #     self.db.execute(req, id)
    #     print("Donnée supprimer ")

    # def modifTouriste(self, nom, prenom, age, id):
    #     reqModif = "UPDATE touriste SET nom = %s, prenom = %s, age = %s WHERE id = %s"
    #     self.db.execute(reqModif, nom, prenom, age, id)
    #     print("Modification réussi ")

    # def listTouriste(self):
    #     query = "SELECT Touriste.id, Touriste.nom, Touriste.prenom, Touriste.age, Groupe.nom_groupe FROM Touriste LEFT JOIN Groupe ON Touriste.groupe_id = Groupe.id"
    #     resultat = self.db.fetchall(query)
    #     for row in resultat:
    #         print(row)
