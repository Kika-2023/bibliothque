import json

def charger_bibliotheque():
    with open("bibliotheque.json", "r") as fichier:
        return json.load(fichier)

def sauvegarder_bibliotheque(bibliotheque):
    with open("bibliotheque.json", "w") as fichier:
        fichier.write(json.dumps(bibliotheque, indent=2))

def afficher_livre(livre):
    print("ID:", livre["ID"])
    print("Titre:", livre["Titre"])
    print("Auteur:", livre["Auteur"])
    print("Annee:", livre["Annee"])
    print("Lu:", livre["Lu"])
    print("Note:", livre["Note"])
    print("Commentaire:", livre["Commentaire"])
    print("---------------")

def afficher_tous(bibliotheque):
    if not bibliotheque:
        print("Aucun livre dans la bibliothèque.")
        return
    for livre in bibliotheque:
        afficher_livre(livre)

def ajouter_livre(bibliotheque):
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    annee = int(input("Annee : "))
    
    id_nouveau = bibliotheque[-1]["ID"] + 1 if bibliotheque else 1

    nouveau_livre = {
        "ID": id_nouveau,
        "Titre": titre,
        "Auteur": auteur,
        "Annee": annee,
        "Lu": False,
        "Note": None,
        "Commentaire": ""
    }

    bibliotheque.append(nouveau_livre)
    sauvegarder_bibliotheque(bibliotheque)
    print("Livre ajouté.\n")

def supprimer_livre(bibliotheque):

    id_sup = int(input("ID à supprimer : "))
    nouveaux = [livre for livre in bibliotheque if livre["ID"] != id_sup]

    if len(nouveaux) == len(bibliotheque):
        print("Aucun livre avec cet ID.")
    else:
        sauvegarder_bibliotheque(nouveaux)
        print("Livre supprimé.")
    return nouveaux

def rechercher_livre(bibliotheque):
    mot = input("Mot-clé à chercher : ").lower()
    trouvés = [livre for livre in bibliotheque if mot in livre["Titre"].lower() or mot in livre["Auteur"].lower()]
    if not trouvés:
        print("Aucun livre trouvé.")
    else:
        for livre in trouvés:
            afficher_livre(livre)

def marquer_comme_lu(bibliotheque):
    id_lu = int(input("ID du livre lu : "))

    for livre in bibliotheque:
        if livre["ID"] == id_lu:
            livre["Lu"] = True
            
            livre["Note"] = float(input("Note sur 10 : "))
            
            livre["Commentaire"] = input("Commentaire : ")
            print("📘 Livre mis à jour.")
            sauvegarder_bibliotheque(bibliotheque)
            return

    print("Livre non trouvé.")

def afficher_selon_etat(bibliotheque, etat_lu):
    trouvés = [livre for livre in bibliotheque if livre["Lu"] == etat_lu]
    if not trouvés:
        print("Aucun livre correspondant.")
    else:
        for livre in trouvés:
            afficher_livre(livre)

def trier_livres(bibliotheque):
    print("1. Trier par Annee")
    print("2. Trier par auteur")
    print("3. Trier par note")
    choix = input("Choix : ")

    if choix == "1":
        livres_tries = sorted(bibliotheque, key=lambda x: x["Annee"])
    elif choix == "2":
        livres_tries = sorted(bibliotheque, key=lambda x: x["Auteur"])
    elif choix == "3":
        livres_tries = sorted(bibliotheque, key=lambda x: (x["Note"] is None, x["Note"]))
    else:
        print("Choix invalide.")
        return

    if not livres_tries:
        print("Aucun livre à trier.")
    else:
        for livre in livres_tries:
            afficher_livre(livre)

def afficher_menu():
    print("\n===== MENU =====")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Rechercher un livre")
    print("4. Afficher tous les livres")
    print("5. Marquer un livre comme lu")
    print("6. Afficher les livres lus")
    print("7. Afficher les livres non lus")
    print("8. Trier les livres")
    print("9. Quitter")

# Programme principal
bibliotheque = charger_bibliotheque()

while True:
    afficher_menu()
    choix = input("Ton choix : ")

    if choix == "1":
        ajouter_livre(bibliotheque)
    elif choix == "2":
        bibliotheque = supprimer_livre(bibliotheque)
    elif choix == "3":
        rechercher_livre(bibliotheque)
    elif choix == "4":
        afficher_tous(bibliotheque)
    elif choix == "5":
        marquer_comme_lu(bibliotheque)
    elif choix == "6":
        afficher_selon_etat(bibliotheque, True)
    elif choix == "7":
        afficher_selon_etat(bibliotheque, False)
    elif choix == "8":
        trier_livres(bibliotheque)
    elif choix == "9":
        break
    else:
        print("Option invalide.")