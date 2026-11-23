from donnees import SESSIONS
from calculs import calculer_revenu, calculer_total_credit, compter_pannes
from affichage import afficher_menu, afficher_sessions

def lancer_jeu():
    while True:
        afficher_menu()
        choix = input("Ton choix (1-5) : ")

        if choix == "1":
            afficher_sessions(SESSIONS)
        elif choix == "2":
            print(f"\nRevenu total : {calculer_revenu(SESSIONS)} FCFA")
        elif choix == "3":
            print(f"\nTotal des credits : {calculer_total_credit(SESSIONS)} FCFA")
        elif choix == "4":
            print(f"\nNombre de pannes : {compter_pannes(SESSIONS)}")
        elif choix == "5":
            print("Merci ! A bientot au Cybercafe de Sossou Grace !")
            break
        else:
            print("Choix invalide, reessaie.")