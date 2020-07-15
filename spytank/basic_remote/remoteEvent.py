#!/usr/bin/env python
import click
import spytank

z= "z: avancer"
s= "s: reculer"
q= "q: tourner a gauche"
d= "d: tourner a droite"
x= "x: stop"
a= "a: augmenter vitesse"
e= "e: diminuer la vitesse"
p= "p: quitter"

print(z,s,q,d,x,a,e,p)
continuer = True
vitesse = 100

while continuer:
    lettre = click.getcha
    if  lettre == "z":
        spytank.avance(vitesse)
    elif lettre == "s":
        spytank.recule(vitesse)
    elif lettre == "x":
        spytank.stop()
    elif lettre == "d":
        spytank.droite(vitesse)
    elif lettre == "q":
        spytank.gauche(vitesse)
    elif lettre =="a":
        if vitesse <100:
            vitesse = vitesse+10
    elif lettre=="e": 
        if vitesse > 0:
            vitesse = vitesse-10
    elif lettre == "p":
        continuer = False
        spytank.stop()  

        