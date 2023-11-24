'''''
#Avec Boucle for
import time

def compte_a_rebours_for(n):
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)


n = int(input("Entrez un nombre entier positif : "))


if n < 0:
    print("Veuillez entrer un nombre entier positif.")
else:
    compte_a_rebours_for(n)
'''
#Sans boucle for
import time

def compte_a_rebours_while(n):
    while n >= 0:
        print(n)
        n -= 1
        time.sleep(1)


n = int(input("Entrez un nombre entier positif : "))


if n < 0:
    print("Veuillez entrer un nombre entier positif.")
else:
    compte_a_rebours_while(n)
