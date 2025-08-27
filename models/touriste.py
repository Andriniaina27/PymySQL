from .database import Database

class Touriste:
    def __init__(self, id, base = Database()):
        # self.db = Database()
        self.id = id
        self.base = base

        if self.base.connexion is not None:
            self.base.cursor.execute("SELECT nom FROM touriste")
            dico = self.base.cursor.fetchone()
            self.nom = dico["nom"]

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
