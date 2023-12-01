def tri_selection(tab):
    n = len(tab)

    for i in range(n - 1):

        min_index = i
        for j in range(i + 1, n):
            if tab[j] < tab[min_index]:
                min_index = j

        tab[i], tab[min_index] = tab[min_index], tab[i]
        print(tab)


liste_exemple = [5, 2, 4, 8, 1, 3]


tri_selection(liste_exemple.copy())


print(sorted(liste_exemple))


liste_exemple.sort()
print(liste_exemple)
