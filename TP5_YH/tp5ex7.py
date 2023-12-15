import os.path
import datetime

def afficher_taille_et_date(fichier):
    taille = os.path.getsize(fichier)
    date_modification = datetime.datetime.fromtimestamp(os.path.getmtime(fichier))
    print(f"Le fichier {fichier} a une taille de {taille} octets.")
    print(f"La dernière modification a eu lieu le : {date_modification}")


fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")


if os.path.isfile(fichier1) and os.path.isfile(fichier2):
    afficher_taille_et_date(fichier1)
    afficher_taille_et_date(fichier2)

    date_modif_fichier1 = os.path.getmtime(fichier1)
    date_modif_fichier2 = os.path.getmtime(fichier2)

    if date_modif_fichier1 > date_modif_fichier2:
        print(f"Le fichier le plus récent est : {fichier1}")
    elif date_modif_fichier1 < date_modif_fichier2:
        print(f"Le fichier le plus récent est : {fichier2}")
    else:
        print("Les deux fichiers ont été modifiés à la même date.")
else:
    print("Certains fichiers n'existent pas.")
