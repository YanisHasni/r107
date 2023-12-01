def find_most_frequent(lst):

    most_frequent = max(set(lst), key=lst.count)
    frequency = lst.count(most_frequent)


    print(f"Le nombre le plus frequent dans la liste est le : {most_frequent} ({frequency} x)")

liste_exemple = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
find_most_frequent(liste_exemple)
