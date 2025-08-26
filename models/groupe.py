from .database import Database

class Groupe:
    def __init__(self):
        self.db = Database()

    def ajoutGroupe(self, nomG):
        requete = "INSERT INTO groupe VALUES(NULL, %s)"
        self.db.execute(requete, nomG)
        print("Groupe ajouté avec succès !")

    def supprGroupe(self, id):
        req = "DELETE FROM groupe WHERE id = %s"
        self.db.execute(req, id)
        print("Donnée supprimer ")

    def modifGroupe(self, nomG, id):
        modif = "UPDATE groupe SET nom_groupe = %s WHERE id = %s"
        self.db.execute(modif, nomG, id)
        print("Modification réussi ")

    def listGroupe(self):
        query = "SELECT * FROM Groupe"
        resultat = self.db.fetchall(query)
        for row in resultat:
            print(row)
