from .database import Database

class Groupe:
    __base = Database()
    def __init__(self, id):
        self.base = Database()
        self.id = id
        self.nom = None

        self.base
        self.base.cursor.execute("SELECT nom_groupe FROM groupe WHERE id = ", (self.id,))
        dico = self.base.cursor.fetchone()

        if dico:
            self.nomG = dico["nom_groupe"]

    def __str__(self):
        chaine = f"ID : {self.id}\n Nom : {self.nom}"
        return chaine
    
    # def __setattr__(self, attr, val):
    #     if attr in ["id", "base", "nom"]:
    #         self.__dict__[attr] = val
    #         self.base.cursor.execute
    
    @classmethod
    def getGrp(cls):
        cls.__base.cursor.execute("SELECT * FROM groupe")
        return cls.__base.cursor.fetchall()

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
