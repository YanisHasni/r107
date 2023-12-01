def multiplication_table(nombre):

    table_resultats = []


    for i in range(10):
        resultat = nombre * i
        table_resultats.append(resultat)


    print(f"Vous cherchez la table de multiplication de quel nombre ? {nombre}")
    for i, resultat in enumerate(table_resultats):
        print(f"{nombre} * {i} = {round(resultat, 1)}")


nombre_utilisateur = float(input("Entrez le nombre pour la table de multiplication : "))

multiplication_table(nombre_utilisateur)
