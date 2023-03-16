#!/usr/bin/env python3

variable = "Salut les gars"
print(variable.replace("les gars", "messieurs dames"))

print(variable.count("a")) 
## return 2 

print(variable.upper())
# return "SALUT LES GARS"

print(variable.index("a"))
# return 1
print(variable.index("u"))
#return 3

print(variable[0])
# return S

liste = ["Magie", "John", "Marc", "Yaya"]
liste.remove("Yaya")
print(liste)
liste.insert(2, "Arthur")
print(liste)
liste.pop()
print(liste)



conversionMois = {
    1: "Janvier",
    2: "Février",
    3: "Avril"
}

print(conversionMois.get(3))
# return avril

