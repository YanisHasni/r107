def taille_chaine(chaine):
    taille = 0
    for char in chaine:
        if char == '\0':  
            break
        taille += 1
    return taille

def pourcentage_voyelles(chaine):
    voyelles = "aeiouyAEIOUY"
    nombre_voyelles = sum(1 for char in chaine if char in voyelles)
    taille = taille_chaine(chaine)
    pourcentage = (nombre_voyelles / max(1, taille)) * 100
    return pourcentage

def recherche_sous_chaine(chaine, sous_chaine):
    taille_ch = taille_chaine(chaine)
    taille_sous_ch = taille_chaine(sous_chaine)

    for i in range(taille_ch - taille_sous_ch + 1):
        match = True
        for j in range(taille_sous_ch):
            if chaine[i + j] != sous_chaine[j]:
                match = False
                break
        if match:
            return i
    return -1

def nombre_occurrences(chaine, sous_chaine):
    count = 0
    index = 0

    while True:
        index = recherche_sous_chaine(chaine[index:], sous_chaine)
        if index == -1:
            break
        count += 1
        index += 1

    return count


chaine_a_traiter = input("Entrez une chaîne de caractères : ")


taille = taille_chaine(chaine_a_traiter)
print(f"La taille de la chaîne est : {taille} caractères.")


pourcentage = pourcentage_voyelles(chaine_a_traiter)
print(f"Le pourcentage de voyelles dans la chaîne est : {pourcentage:.2f}%.")


debut_occurrence = recherche_sous_chaine(chaine_a_traiter, 'wagon')
if debut_occurrence != -1:
    print(f"La sous-chaîne 'wagon' commence à la position : {debut_occurrence}.")
else:
    print("La sous-chaîne 'wagon' n'est pas présente dans la chaîne.")


occurrences = nombre_occurrences(chaine_a_traiter, 'wagon')
print(f"Le nombre d'occurrences de la sous-chaîne 'wagon' est : {occurrences}.")
