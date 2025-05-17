from gestion_bibliotheque import *

def afficher_menu():
    print("\n📚 MENU")
    print("1. Afficher tous les livres")
    print("2. Ajouter un livre")
    print("8. Quitter")

def boucle_principale():
    biblio = charger_bibliotheque()
    print("Bienvenue Mohib Eddine Bekkai dans votre bibliothèque 📚")

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            print(biblio)
        elif choix == "2":
            ajouter_livre(biblio)
        elif choix == "8":
            sauvegarder_bibliotheque(biblio)
            print("📁 Données sauvegardées. À bientôt !")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    boucle_principale()
