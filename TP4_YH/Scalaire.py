3
nMax = 10


while True:
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
    if 1 <= n <= nMax:
        break
    else:
        print(f"Veuillez entrer une valeur entre 1 et {nMax}.")


v1 = []
v2 = []


print("Saisie du premier vecteur :")
for i in range(n):
    v1.append(int(input(f"v1[{i}] = ")))


print("Saisie du second vecteur :")
for i in range(n):
    v2.append(int(input(f"v2[{i}] = ")))


produit_scalaire = sum(x * y for x, y in zip(v1, v2))


print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}.")
