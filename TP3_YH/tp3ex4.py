def factorielle_for(n):
    if n < 0:
        return "Impossible de calculer la factorielle d'un nombre négatif."

    resultat = 1
    print(f"Calcul de la factorielle de {n} avec une boucle 'for':")
    for i in range(1, n + 1):
        resultat *= i
        print(f"Étape {i}: {resultat}")
    return resultat


def factorielle_while(n):
    if n < 0:
        return "Impossible de calculer la factorielle d'un nombre négatif."

    resultat = 1
    i = 1
    print(f"Calcul de la factorielle de {n} avec une boucle 'while':")
    while i <= n:
        resultat *= i
        print(f"Étape {i}: {resultat}")
        i += 1
    return resultat



n = int(input("Entrez un nombre entier : "))


choix_boucle = input("Choisissez la boucle à utiliser ('for' ou 'while') : ").lower()


if choix_boucle == 'for':
    resultat = factorielle_for(n)
elif choix_boucle == 'while':
    resultat = factorielle_while(n)
else:
    resultat = "Choix de boucle non valide. Veuillez choisir 'for' ou 'while'."


print(f"La factorielle de {n} est : {resultat}")
