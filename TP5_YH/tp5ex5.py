def calculer_salaire(nombre_heures, salaire_horaire):
    heures_normales = min(nombre_heures, 160)
    heures_majoration1 = max(0, min(nombre_heures - 160, 40))
    heures_majoration2 = max(0, nombre_heures - 200)

    salaire_normal = heures_normales * salaire_horaire
    salaire_majoration1 = heures_majoration1 * salaire_horaire * 1.25
    salaire_majoration2 = heures_majoration2 * salaire_horaire * 1.5

    salaire_total = salaire_normal + salaire_majoration1 + salaire_majoration2

    return salaire_total


nombre_heures = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))


salaire_resultat = calculer_salaire(nombre_heures, salaire_horaire)


print(f"Le salaire total est de {salaire_resultat:.2f} euros.")
