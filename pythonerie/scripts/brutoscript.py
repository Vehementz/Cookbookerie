#!/usr/bin/env python3

import random
import time
import string
import hashlib
import sys
import argparse

parser = argparse.ArgumentParser(description="Password cracker ")
parser.add_argument("-f", "--file", dest="file", help="Path of the dictionary file")  
parser.add_argument("-g", "--gen", dest="gen", help="Generate MD5 hash of password")  
parser.add_argument("--md5", dest="md5", help="hashed password (MD5)", required=False)

args = parser.parse_args()
print(args.file)

# Guess password

mot_de_passe = input("Quel est le mot de passe ? :")
mot_de_passe_md5 = hashlib.md5(mot_de_passe.encode('utf8')).hexdigest()
print(mot_de_passe_md5)


def crack_dict(md5, file):
    try:
        for mot in file.readlines():
            mot = mot.strip("\n").encode("utf8")
            hashmd5 = hashlib.md5(mot).hexdigest()
            if hashmd5 == md5:
                print("Mot de passe trouvé : " +
                      str(mot) + " (" + hashmd5 + ")")
                trouve = True
        if not trouve:
            print("Mot de passe non trouvé :(")
        file.close()
    except FileNotFoundError:
        print("Erreur : nom de dossier ou fichier introuvable !")
        sys.exit(1)
    except Exception as err:
        sys.exit(1)
        

debut = time.time()
crack_dict()

# fin = time.time()

print("durée : " + str(time.time() - debut) + " secondes")
# test
def mot_aleatoire():
    lettres = string.ascii_letters
    suiv = ""
    resultat = ""
    for i in range(len(mot_de_passe)):
        while mot_de_passe[i] != suiv:
            suiv = random.choice(lettres)        
            suiv = random.choice(lettres)
        resultat += suiv


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



# First program
# import random
# import time

# mot_de_passe = "mdpe" 
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

