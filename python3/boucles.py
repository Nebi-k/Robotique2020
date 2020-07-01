# il existe 2 types de boucles en python
# for ... in ... : pour chaqque element dans une suite, fais...
# while() : "tant que" la condition est vrai, fais ....

i = 1 # i pour imcrement par convention
fin = 10

while (i<= fin):
    print("compteur =",i)
    i = i + 1

texte = "quarante"

#for lettre in texte :
 #   print(lettre)

nb_voyelles = 0
nb_consonnes = 0


for lettre in texte :
    if lettre in "aeiouy" :
        print(lettre)


for lettre in texte :
    if lettre in "aeiouy" :
        nb_voyelles = nb_voyelles +1
    else : 
        nb_consonnes = nb_consonnes + 1

print("consonnes = ", nb_consonnes)
print("voyelles =", nb_voyelles)