import click
from gtts import gTTS
import os
import network

ADDRESS = "10.0.0.111"
PORT = 1111

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
while continuer:
    socket = network.newClientSocket()
    socket.connect((ADDRESS, PORT))

    print("tapez votre lette")
    lettre = click.getchar()

    socket.send(lettre.encode())
    if lettre == "p":
        continuer = False
