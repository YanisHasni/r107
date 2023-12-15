def saisie_personne():
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    return nom, prenom

def afficher_resultat(nom, prenom):
    nom_majuscules = nom.upper()
    prenom_capitalized = prenom.capitalize()

    print(f"{prenom_capitalized} {nom_majuscules}")


nom1, prenom1 = saisie_personne()


nom2, prenom2 = saisie_personne()


if nom1 == nom2:
    if prenom1 <= prenom2:
        afficher_resultat(nom1, prenom1)
        afficher_resultat(nom2, prenom2)
    else:
        afficher_resultat(nom2, prenom2)
        afficher_resultat(nom1, prenom1)
else:
    if nom1 <= nom2:
        afficher_resultat(nom1, prenom1)
        afficher_resultat(nom2, prenom2)
    else:
        afficher_resultat(nom2, prenom2)
        afficher_resultat(nom1, prenom1)
