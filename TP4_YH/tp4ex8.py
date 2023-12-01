# 5 Enregistrement des données dans un dictionnaire
etudiant = {
    "name": "HASNI",
    "firstname": "Yanis",
    "promo": 2023,
    "group": "RT112"
}

# Affichage des données
print(f"Votre nom est '{etudiant['name']}', prénom est '{etudiant['firstname']}', vous faites "
      f"partie de la promo '{etudiant['promo']}' et votre groupe est '{etudiant['group']}'")

# 6 Affichage du contenu du dictionnaire
dic = {"name": "Yanis", "firstname": "HASNI", "promo": 2022, "group": 202}

print("\nLes clés du dictionnaire sont :")
for key in dic.keys():
    print(f"-{key}")

print("\nLes valeurs du dictionnaire sont :")
for value in dic.values():
    print(f"-{value}")

print("\nLes tuplets du dictionnaire sont :")
for item in dic.items():
    print(f"-{item}")

# 7 Ajout d'un autre dictionnaire pour une autre personne
autre_etudiant = {"name": "tata", "firstname": "tutu", "promo": 2022, "group": 102}

# 8 Création d'un dictionnaire binôme
binome = {
    "identifiant1": etudiant,
    "identifiant2": autre_etudiant
}

# 9 Affichage des membres du binôme
print("\nLes étudiants formant le binôme sont :")
for identifiant, etudiant_binome in binome.items():
    print(f"- L'étudiant {etudiant_binome['name']} {etudiant_binome['firstname']} du groupe {etudiant_binome['group']}")
