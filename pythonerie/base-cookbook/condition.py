#!/usr/bin/env python3

age = 10
homme = True

if age >= 18 and homme:
    print("Un homme majeur")
elif age <= 18 and homme:
    print("Un homme mineur")
elif age >= 18 and not homme:
    print("Une femme majeure")
elif age <= 18 and not homme:
    print("Une femme mineure")   