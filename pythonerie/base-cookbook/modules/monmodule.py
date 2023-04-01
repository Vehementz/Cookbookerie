#!/usr/bin/python3

mavariable = "La variable du module"

print("Je suis {}".format(mavariable))

def mafonction(defaut = mavariable):
    return "Fonction du module : {}".format(defaut) 