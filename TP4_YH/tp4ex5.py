def est_annee_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def verifier_date(date):
    if len(date) != 8:
        print("Format de date incorrect. Veuillez saisir une date au format jjmmaaaa.")
        return

    jour = int(date[:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    if mois < 1 or mois > 12:
        print("Mois invalide. Veuillez saisir un mois entre 01 et 12.")
    elif jour < 1 or jour > 31:
        print("Jour invalide. Veuillez saisir un jour entre 01 et 31.")
    elif mois in [4, 6, 9, 11] and jour > 30:
        print(f"Mois {mois} ne peut pas avoir plus de 30 jours.")
    elif mois == 2:
        if (est_annee_bissextile(annee) and jour > 29) or (not est_annee_bissextile(annee) and jour > 28):
            print(f"Février {annee} ne peut pas avoir plus de {29 if est_annee_bissextile(annee) else 28} jours.")
        else:
            print("Date valide.")
    elif jour > 31:
        print(f"Mois {mois} ne peut pas avoir plus de 31 jours.")
    else:
        print("Date valide.")


date_saisie = input("Veuillez saisir une date au format jjmmaaaa : ")
verifier_date(date_saisie)

