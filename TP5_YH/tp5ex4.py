def decomposer_somme(somme):
    valeurs = [100, 50, 10, 2, 1]


    decomposition = {}


    for valeur in valeurs:
        nombre_billets_pieces = somme // valeur
        if nombre_billets_pieces > 0:
            decomposition[valeur] = nombre_billets_pieces
            somme %= valeur

    return decomposition

def afficher_decomposition(somme, decomposition):

    message = f"{somme} euros, c'est donc"
    for valeur, nombre in decomposition.items():
        if nombre > 0:
            message += f" {nombre} {'billet' if valeur >= 10 else 'pièce'}{'s' if nombre > 1 else ''} de {valeur},"
    message = message.rstrip(',') + "."
    print(message)


somme = int(input("Entrez une somme d'argent en euros : "))

decomposition_result = decomposer_somme(somme)

afficher_decomposition(somme, decomposition_result)
