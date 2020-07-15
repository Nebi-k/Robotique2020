#!/usr/bin/env python
import spytank
spytank.init()
print("Utiliser les touches ZQSD pour le manipuler")
print("Taper X pour arreter le robot")
lettre = input(">> ")

while True:
    if lettre == "z":
        spytank.avance(100)
    elif lettre == "s":
        spytank.recule(100)
    elif lettre == "x":
        spytank.stop()
    elif lettre == "d":
        spytank.droite(100)
    elif lettre == "q":
        spytank.gauche(100)
        