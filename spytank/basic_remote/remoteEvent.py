#!/usr/bin/env python
import click
import spytank

spytank.init()

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
direction =1

while continuer:
    lettre = click.getchar()
    if  lettre == "z":
        spytank.avance(vitesse)
        direction = 1
    elif lettre == "s":
        spytank.recule(vitesse)
        direction = 2
    elif lettre == "x":
        spytank.stop()
        direction = 5
    elif lettre == "d":
        spytank.droite(vitesse)
        direction = 4
    elif lettre == "q":
        spytank.gauche(vitesse)
        direction = 3

    elif lettre =="a":
        if vitesse <100:
            vitesse = vitesse+10
        if direction ==1:
            spytank.avance(vitesse)
        
        elif  direction== 2:
            spytank.recule(vitesse)
        elif direction== 3:
            spytank.gauche(vitesse)
        elif direction== 4:
            spytank.droite(vitesse)
        elif direction== 5:
            spytank.stop()
            
          
    elif lettre=="e": 
        if vitesse > 0:
            vitesse = vitesse-10
        if direction ==1:
            spytank.avance(vitesse)
        
        elif  direction== 2:
            spytank.recule(vitesse)
        elif direction== 3:
            spytank.gauche(vitesse)
        elif direction== 4:
            spytank.droite(vitesse)
        elif direction== 5:
            spytank.stop()
    elif lettre == "p":
        continuer = False
        spytank.stop()  

        