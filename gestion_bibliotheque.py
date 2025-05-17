import json
import os

FICHIER = "bibliotheque.json"

def charger_bibliotheque():
    if os.path.exists(FICHIER):
        with open(FICHIER, "r") as f:
            return json.load(f)
    return []

def sauvegarder_bibliotheque(biblio):
    with open(FICHIER, "w") as f:
        json.dump(biblio, f, indent=4)
def generer_id(biblio):
    if not biblio:
        return 1
    return max(livre["ID"] for livre in biblio) + 1

def ajouter_livre(biblio):
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    annee = input("Année : ")
    livre = {
        "ID": generer_id(biblio),
        "Titre": titre,
        "Auteur": auteur,
        "Année": int(annee),
        "Lu": False,
        "Note": None,
        "Commentaire": ""
    }
    biblio.append(livre)
    print("✅ Livre ajouté avec succès !")
def afficher_livres(biblio):
    if not biblio:
        print("📚 La bibliothèque est vide.")
        return

    for livre in biblio:
        etat = "✔ Lu" if livre["Lu"] else "✖ Non lu"
        print(f"\nID: {livre['ID']}")
        print(f"Titre: {livre['Titre']}")
        print(f"Auteur: {livre['Auteur']}")
        print(f"Année: {livre['Année']}")
        print(f"État: {etat}")
        if livre["Lu"]:
            print(f"Note: {livre['Note']}/10")
            print(f"Commentaire: {livre['Commentaire']}")
def supprimer_livre(biblio):
    try:
        id_sup = int(input("ID du livre à supprimer: "))
    except ValueError:
        print("❌ ID invalide.")
        return

    for livre in biblio:
        if livre["ID"] == id_sup:
            confirmation = input(f"Confirmer la suppression de '{livre['Titre']}' ? (o/n): ").lower()
            if confirmation == 'o':
                biblio.remove(livre)
                print("🗑 Livre supprimé.")
            else:
                print("❎ Suppression annulée.")
            return

    print("❌ Livre non trouvé.")
def rechercher_livre(biblio):
    mot_cle = input("Entrez un mot-clé (titre ou auteur) : ").lower()
    resultats = [livre for livre in biblio if mot_cle in livre["Titre"].lower() or mot_cle in livre["Auteur"].lower()]

    if resultats:
        print(f"\n🔍 {len(resultats)} résultat(s) trouvé(s) :")
        afficher_livres(resultats)
    else:
        print("❌ Aucun livre trouvé.")
def marquer_comme_lu(biblio):
    try:
        id_livre = int(input("ID du livre lu: "))
    except ValueError:
        print("❌ ID invalide.")
        return

    for livre in biblio:
        if livre["ID"] == id_livre:
            livre["Lu"] = True
            try:
                note = int(input("Note sur 10 : "))
                if note < 0 or note > 10:
                    print("❌ Note invalide.")
                    return
            except ValueError:
                print("❌ Note invalide.")
                return
            commentaire = input("Commentaire : ")
            livre["Note"] = note
            livre["Commentaire"] = commentaire
            print("📘 Livre marqué comme lu.")
            return

    print("❌ Livre non trouvé.")
def filtrer_par_etat(biblio):
    choix = input("Afficher les livres (l) lus ou (n) non lus ? ").lower()
    if choix == 'l':
        livres_lus = [livre for livre in biblio if livre["Lu"]]
        afficher_livres(livres_lus)
    elif choix == 'n':
        livres_non_lus = [livre for livre in biblio if not livre["Lu"]]
        afficher_livres(livres_non_lus)
    else:
        print("❌ Choix invalide.")
def trier_livres(biblio):
    print("Trier par : 1) Auteur  2) Année  3) Note")
    choix = input("Votre choix : ")

    if choix == '1':
        livres_tries = sorted(biblio, key=lambda x: x["Auteur"])
    elif choix == '2':
        livres_tries = sorted(biblio, key=lambda x: x["Année"])
    elif choix == '3':
        livres_tries = sorted(biblio, key=lambda x: (x["Note"] if x["Note"] is not None else -1), reverse=True)
    else:
        print("❌ Choix invalide.")
        return

    afficher_livres(livres_tries)
