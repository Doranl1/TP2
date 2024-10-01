"""
Exercice: TP2
Nom: Liam Doran
Groupe: 404
"""
import random
borne_minimum = 0
borne_maximum = 100
jeu = 0


def borne_choisi():
    borne_minimum_usager = int(input("quel est le minimum?\n"))
    borne_maximum_usager = int(input("quel est le minimum?\n"))
    return borne_minimum_usager, borne_maximum_usager


while jeu == 0:
    # choisir si l'usager veut choisir le borne
    borne_usager = str(input("voulez-vous choisir le minimum et maximum?\n"))
    if borne_usager == "oui":
        borne_minimum, borne_maximum = borne_choisi()
    else:
        print("\n")
    # intro du jeu
    choix = -1
    print(f"J’ai choisi un nombre au hasard entre {borne_minimum} et {borne_maximum}.\nÀ vous de le deviner...\n")
    choix2 = random.randint(borne_minimum, borne_maximum)
    while choix != choix2:  # début du jeu
        choix = int(input("Entrez votre essai :\n"))
        if choix > choix2:  # le choix est grande
            print("%d est plus grand" % choix)
        elif choix < choix2:  # le chois est petit
            print("%d est plus petit" % choix)
        elif choix == choix2:  # la victiore de l'usager
            print("bravo, vous avez gagner")
            choix = choix2
    # rejouer
    jeu = str(input("veut-tu rejouer?"))
    if jeu == "oui" or jeu == "Oui":
        jeu = 0
    else:
        print("bye")
        break
