"""
Exercice: TP2
Nom: Liam Doran
Groupe: 404
"""
import random
minimum = 0
maximum = 100
def choix_usager(minimum, maximum):
    minimum = int(input("choisi un nombre. ce sera le minimum"))
    maximum = int(input("choisi un nombre. ce sera le maximum"))
    return (minimum, maximum)

minimum, maximum = choix_usager(minimum, maximum)

jouer = 0
jeu = "a"
while jouer == 0:
    choix = -1
    print(f"J’ai choisi un nombre au hasard entre {minimum} et {maximum}.\nÀ vous de le deviner...\n")
    choix2 = random.randint(minimum, maximum)
    while choix != choix2:
        choix = int(input("Entrez votre essai :   "))
        if choix > choix2:
            print("%d est plus grand" % choix)
        elif choix < choix2:
            print("%d est plus petit" % choix)
        elif choix == choix2:
            print("bravo...")
            choix = choix2
    jeu = str(input("veut-tu rejouer?"))
    if jeu == "oui" or jeu == "Oui":
        jeu = 0
    else:
        print("ok")
        break
