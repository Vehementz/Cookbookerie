#!/usr/bin/env python3

import random
import time

import string

### nombre aléatoire
# print(random.randint(0, 244)) 



#### Guess password

mot_de_passe = input("Quel est le mot de passe ? :")

# test
def mot_aleatoire():
    lettres = string.ascii_letters
    suiv = ""
    resultat = ""
    for i in range(len(mot_de_passe)):
        while mot_de_passe[i] != suiv:
            suiv = random.choice(lettres)        
        resultat += suiv        
    return resultat

debut = time.time()
mot_aleatoire()
print("Durée: " + str(time.time() - debut) + " secondes")


# while True:
#     mot_alea = mot_aleatoire(len(mot_de_passe))
#     print("Mot de passe testé: " + mot_alea)
#     if mot_de_passe == mot_alea:
#         print("Mot de passe trouvé !" + mot_alea)
#         fin = time.time() - debut
#         print("Mot de passe trouvé ! en " + str(fin) + " secondes" + mot_alea)
#         break




##### First program

# import random
# import time

# mot_de_passe = "mdpe" 



# def mot_aleatoire(longeur):
#     lettres =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     mot_genere = ""
#     for carac in range(0, longeur):
#         mot_genere = mot_genere + lettres[random.randint(0, len(lettres) -1)]
#     return mot_genere

# print(mot_aleatoire(4))


# debut = time.time()
# while True:
#     mot_alea = mot_aleatoire(len(mot_de_passe))
#     print("Mot de passe testé: " + mot_alea)
#     if mot_de_passe == mot_alea:
#         print("Mot de passe trouvé !" + mot_alea)
#         fin = time.time() - debut
#         print("Mot de passe trouvé ! en " + str(fin) + " secondes" + mot_alea)
#         break



