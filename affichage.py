def afficher_menu():
    print("\n--- CYBERCAFE DE SOSSOU GRACE ---")
    print("1. Voir toutes les sessions")
    print("2. Voir le revenu total")
    print("3. Voir le total des credits")
    print("4. Voir le nombre de pannes")
    print("5. Quitter")

def afficher_sessions(sessions):
    print("\n--- LISTE DES SESSIONS ---")
    for s in sessions:
        etat = "Paye" if s["paye"] else "Credit"
        print(f"{s['client']} - Poste {s['poste']} - {s['duree']}h - {s['prix']} FCFA - {etat} - Credit: {s['credit']} - Panne: {s['panne']}")