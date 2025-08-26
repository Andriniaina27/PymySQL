from models.groupe import Groupe
from models.touriste import Touriste

def main():
    
    grp = Groupe()
    touriste = Touriste()

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Groupe")
        print("2. Touriste")
        choixBase = input("Entrez une option 1 ou 2 : ")

        match choixBase:
            case "1":
                print("\n--- MENU GROUPE ---")
                print("1. Ajout")
                print("2. Voir la liste")
                print("3. Suppression")
                print("4. Modification")
                choixgrp = input("Entrez une option: ")
                match choixgrp:
                    case "1":
                        print("\n--- Ajout Groupe ---")
                        nomG = input("Nom Groupe : ")
                        grp.ajoutGroupe(nomG)
                    case "2":
                        print("\n--- Liste Groupe ---")
                        grp.listGroupe()
                    case "3":
                        print("\n--- Suppression Groupe ---")
                        id = input("Tapez l'ID : ")
                        print("Voulez-vous vraiment supprimer ?")
                        c = input("Oui(O) ou Non(N) : ")
                        if c == "O":
                            grp.supprGroupe(id)
                            print("Donnée supprimer ")
                        else:
                            pass
                    case "4":
                        print("\n--- Modification Groupe ---")
                        nomG = input("Nom Groupe : ")
                        id = input("Tapez l'ID : ")
                        print("Voulez-vous vraiment modifier ?")
                        c = input("Oui(O) ou Non(N) : ")
                        if c == "O":
                            grp.modifGroupe(nomG, id)
                            print("Modification réussi ")
                        else:
                            pass
                        

            case "2":
                print("\n--- MENU TOURISTE ---")
                print("1. Ajout")
                print("2. Voir la liste")
                print("3. Suppression")
                print("4. Modification")
                choixT = input("Entrez une option : ")
                match choixT:
                    case "1":
                        print("\n--- Ajout Touriste ---")
                        nom = input("Nom       : ")
                        prenom = input("Prenom    : ")
                        age = int(input("Age       : "))
                        groupe_id = int(input("Groupe_id : "))
                        touriste.ajoutTouriste(nom, prenom, age, groupe_id)
                    case "2":
                        print("\n--- Liste Touriste ---")
                        touriste.listTouriste()
                    case "3":
                        print("\n--- Suppression Touriste ---")
                        id = input("Entrer l'ID  : ")
                        print("Voulez-vous vraiment supprimer ?")
                        c = input("Oui(O) ou Non(N) : ")
                        if c == "O":
                            touriste.supprimerTouriste(id)
                            print("Donnée supprimer ")
                        else:
                            pass
                        
                    case "4":
                        print("\n--- Modification Touriste ---")
                        nom = input("Nom       : ")
                        prenom = input("Prenom    : ")
                        age = int(input("Age       : "))
                        id = int(input("Id_Tourtiste : "))
                        print("Voulez-vous vraiment modifier ?")
                        c = input("Oui(O) ou Non(N) : ")
                        if c == "O":
                            touriste.modifTouriste(nom, prenom, age, id)
                            print("Modification réussi ")
                        else:
                            pass
                    case "_":
                        print("Choix Indisponible.......")
                        

        choix = input("Voulez-vous continuer ? (O/N): ")
        if choix.upper() != "O":
            break

    print("Fin du programme....")

if __name__ == "__main__":
    main()