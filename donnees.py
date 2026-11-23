# Donnees du Cybercafe de Sossou Grace
# 30 sessions : client, poste, duree, prix, paye, credit, panne

SESSIONS = []

noms = ["Aline", "Boris", "Chloe", "David", "Emma", "Fabrice", "Gloria", "Hugo", "Iris", "Joel",
        "Karen", "Leo", "Mia", "Noah", "Olga", "Paul", "Queen", "Rudy", "Sara", "Theo",
        "Uma", "Victor", "Wendy", "Xavier", "Yann", "Zoe", "Annie", "Bruno", "Carla", "Denis"]

for i in range(30):
    credit = 0
    paye = True
    if (i + 1) % 3 == 0:
        credit = 1000
        paye = False
    panne = False
    if (i + 1) % 5 == 0:
        panne = True
    SESSIONS.append({
        "client": noms[i],
        "poste": (i % 10) + 1,
        "duree": (i % 3) + 1,
        "prix": 1000 * ((i % 3) + 1),
        "paye": paye,
        "credit": credit,
        "panne": panne
    })