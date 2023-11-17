import random
def lancer_piece_truquee():
    resultat = random.randint(0, 2)

    if resultat < 2:
        print("Pile !")
    else:
        print("Face !")

for _ in range(10):
    lancer_piece_truquee()
