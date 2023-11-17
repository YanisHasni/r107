import random

resultat = random.randint(0, 100)

if resultat < 50:
    print("Pile !", resultat)
else:
    print("Face !", resultat)
