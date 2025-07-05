#!/usr/bin/env python


# x = 5
# y = x
# print(id(x))
# print(id(y))
# y = y + 1
# print(id(x))
# print(id(y))



##### Avec une liste

x = [5]
y = x
print(id(x))
print(id(y))
x.append(8)
print(id(x))
print(id(y))
print(x)
print(y)


# un type immutable est automatiquement copié lorsqu’il est modifié,
# un type mutable n’est jamais copié et l’opérateur = crée systématiquement des références entre des variables, pas des copies.