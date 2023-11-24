#Petit A
N = int(input("Entrez la valeur de N : "))
somme = 0

for i in range(N + 1):
    somme += i

print("La somme des N premiers entiers naturels est :", somme)


#Petit B

valeur = 0

while valeur != 100:
    valeur = int(input("Entrez une valeur (entrez 100 pour terminer) : "))

print("La boucle d'attente est terminée.")

#Petit C
valeurs_inf_10 = 0
valeurs_10_a_15 = 0
valeurs_sup_15 = 0

for _ in range(10):
    valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))

    while valeur < 0 or valeur > 20:
        valeur = float(input("La valeur doit être entre 0 et 20. Réessayez : "))

    if valeur < 10:
        valeurs_inf_10 += 1
    elif valeur < 15:
        valeurs_10_a_15 += 1
    else:
        valeurs_sup_15 += 1

print("Nombre de valeurs inférieures à 10 :", valeurs_inf_10)
print("Nombre de valeurs entre 10 (inclus) et 15 (non inclus) :", valeurs_10_a_15)
print("Nombre de valeurs supérieures ou égales à 15 :", valeurs_sup_15)

#Petit D
X = float(input("Entrez la valeur de X (supérieure à 1) : "))
N = 0
somme = 0

while somme <= X:
    N += 1
    somme += N

print("Le plus grand nombre N tel que la somme soit inférieure ou égale à X est :", N - 1)
