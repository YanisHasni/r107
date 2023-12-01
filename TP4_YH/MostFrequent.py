L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
def find_most_frequent(lst):

    occurrences = {}


    for num in lst:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1


    most_frequent = max(occurrences, key=occurrences.get)
    frequency = occurrences[most_frequent]


    print(f"Le nombre le plus frequent dans la liste est le : {most_frequent} ({frequency} x)")


liste_exemple = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
find_most_frequent(liste_exemple)






"""""** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""""
