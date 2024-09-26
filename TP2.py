"""
Exercice: TP2
Nom: Liam Doran
Groupe: 404
"""
import random
borne_minimum = 0
borne_maximum = 100
jeu = 0


while jeu == 0:
    borne_usager = str(input("voulez-vous choisir le minimum et maximum?\n"))
    if borne_usager == "oui":
        borne_minimum = int(input("quel est le minimum?\n"))
        borne_maximum = int(input("quel est le minimum?\n"))
    else:
        print("\n")
    choix = -1
    print(f"J’ai choisi un nombre au hasard entre {borne_minimum} et {borne_maximum}.\nÀ vous de le deviner...\n")
    choix2 = random.randint(borne_minimum, borne_maximum)
    while choix != choix2:
        choix = int(input("Entrez votre essai :\n"))
        if choix > choix2:
            print("%d est plus grand" % choix)
        elif choix < choix2:
            print("%d est plus petit" % choix)
        elif choix == choix2:
            print("bravo, vous avez gagner")
            choix = choix2
    jeu = str(input("veut-tu rejouer?"))
    if jeu == "oui" or jeu == "Oui":
        jeu = 0
    else:
        print("bye")
        break
