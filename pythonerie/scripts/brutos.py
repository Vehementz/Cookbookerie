#!/usr/bin/env python3

import random

mot_de_passe = "mdp" 


### nombre aléatoire
# print(random.randint(0, 244)) 

def mot_aleatoire(longeur):
    lettres =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mot_genere = ""
    for carac in range(0, longeur):
        mot_genere = mot_genere + lettres[random.randint(0, len(lettres) -1)]
    return mot_genere

print(mot_aleatoire(3))

while True:
    mot_alea = mot_aleatoire(len(mot_de_passe))
    print("Mot de passe testé: " + mot_alea)
    if mot_de_passe == mot_alea:
        print("Mot de passe trouvé !" + mot_alea)
        break

