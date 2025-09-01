from .model import Model

class Groupe(Model):
    def __init__(self, id):
        self.id = id
        # self.nom = None

        # self.base
        # self.base.cursor.execute("SELECT nom_groupe FROM groupe WHERE id = ", (self.id,))
    
        dico = Groupe.getById(id)

        # if dico:
        dict = dico
        print(dict)
        # self.nomG = dico["nomG"]
        # self.membres = dict()

    # def __str__(self):
    #     chaine = f"ID : {self.id}\n Nom : {self.nom}"
    #     return chaine
    

    # def getAll(self):
    #     dico = Groupe.getAll()
    #     print(dico)
    # @classmethod
    # def getAll(cls):
    #     cls.__base.cursor.execute("SELECT * FROM groupe")
    #     return cls.__base.cursor.fetchall()
    
    # @classmethod
    # def getById(cls, id):
    #     cls.__base.cursor.execute("SELECT * FROM groupe WHERE id = %s", (id,))
    #     return cls.__base.cursor.fetchone()
    
    # @classmethod
    # def insert(cls, nom):
    #     cls.__base.cursor.execute("INSERT INTO groupe VALUES(NULL, %s)", (nom))
    #     cls.__base.connexion.commit()
    
    # @classmethod
    # def delete(cls,nom, id):
    #     cls.__base.cursor.execute("UPDATE groupe SET nom_groupe = %s WHERE id = %s",(nom,id,))
    #     cls.__base.connexion.commit()

    # def ajoutGroupe(self, nomG):
    #     requete = "INSERT INTO groupe VALUES(NULL, %s)"
    #     self.db.execute(requete, nomG)
    #     print("Groupe ajouté avec succès !")

    # def supprGroupe(self, id):
    #     req = "DELETE FROM groupe WHERE id = %s"
    #     self.db.execute(req, id)
    #     print("Donnée supprimer ")

    # def modifGroupe(self, nomG, id):
    #     modif = "UPDATE groupe SET nom_groupe = %s WHERE id = %s"
    #     self.db.execute(modif, nomG, id)
    #     print("Modification réussi ")

    # def listGroupe(self):
    #     query = "SELECT * FROM Groupe"
    #     resultat = self.db.fetchall(query)
    #     for row in resultat:
    #         print(row)
