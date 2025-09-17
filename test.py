from models.touriste import Touriste

touriste = Touriste.getAllJoin(
    joins=[("groupe", "touriste.groupe_id = groupe.id_groupe")],
    colonne=[("touriste.nom", "touriste.prenom", "touriste.age", "groupe.nomG as nomGrp")]
)

for t in touriste:
    print(t)