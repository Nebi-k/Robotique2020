#!/usr/bin/env python
import spytank

spytank.init() 
vitesse= 100
direction =1

def commande(lettre):
    global vitesse
    global direction
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
        spytank.stop()  

        