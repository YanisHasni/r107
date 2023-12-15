def est_palindrome(chaine):
    chaine_epuree = ''.join(c.lower() for c in chaine if c.isalpha())


    return chaine_epuree == chaine_epuree[::-1]


entree = input("Entrez un mot ou une phrase : ")


if est_palindrome(entree):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
