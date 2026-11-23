def calculer_revenu(sessions):
    total = 0
    for s in sessions:
        if s["paye"]:
            total += s["prix"]
    return total

def calculer_total_credit(sessions):
    total = 0
    for s in sessions:
        total += s["credit"]
    return total

def compter_pannes(sessions):
    total = 0
    for s in sessions:
        if s["panne"]:
            total += 1
    return total