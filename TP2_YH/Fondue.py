BASE = 4

fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de convives pour lesquels vous voulez préparer la fondue : "))

nouveauFromage = fromage * nbConvives / BASE
nouvelleEau = eau * nbConvives / BASE
nouvelAil = ail * nbConvives / BASE
nouveauPain = pain * nbConvives / BASE
print("\nRecette pour", nbConvives, "convives :")
print("- Fromage :", round(nouveauFromage, 2), "grammes")
print("- Eau :", round(nouvelleEau, 2), "décilitres")
print("- Ail :", round(nouvelAil, 2), "gousses")
print("- Pain :", round(nouveauPain, 2), "grammes")
