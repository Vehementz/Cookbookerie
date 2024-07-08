#!/usr/bin/python3


# # # Only args
# def mafonction(*args):
#     liste = []
#     for arg in args:
#         liste.append(" {} Christophoe !!!".format(arg))
#     return liste
# m = mafonction("Hello", "Salut", "Bye Bye")
# print(m)


# # # args and kwargs


def mafonction(*args, **kwargs):
    liste = []
    for arg in args:
        for clef, valeur in kwargs.items():
            liste.append(" {} : ma clef =  {} / ma valeur = {}  !!!".format(arg, clef, valeur))
    return liste
m = mafonction("Hello", "Salut", "Bye Bye", nom="Bruce", ville="Varsovie")
print(m)
