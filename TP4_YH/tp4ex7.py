#partie1
binome = ('Yanis',1, 'jules',2)
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

#Partie 2
nouveau_login = input("Entrez le nouveau login : ")
binome = (binome[0], nouveau_login)
print(f"Nouveau binôme : l'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

#Partie 3
troisieme_login = input("Entrez le troisième login : ")
binome = binome + (troisieme_login,)
print(f"Trinôme : {binome}")
