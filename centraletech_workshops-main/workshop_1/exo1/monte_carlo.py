"""
Le but de cet exercice est d'approximer la valeur de π (pi) avec la méthode de Monte Carlo : 
nous utiliserons deux modules pour cela : random math
random : module qui met à disposition des méthodes liées à l'aléatoire, comment la génération de nombres aléatoires
    (1) random.random() : génére un nombre aléatoire entre 0 et 1
math : module qui met à disposition des méthodes liées aux mathématiques
    (1) math.sqrt(<nombre positif>) : renvoie la racine carré du nombre

Voir le fichier 'monte_carlo_explication.md' pour les étape de l'exercice
"""
from random import random
from math import sqrt
import math
L=[(random(),random()) for i in range (200000)]
nb_pts_interieurs=0
for i in L:
    if sqrt((i[1]**2)+(i[0]**2))<=1 :
        nb_pts_interieurs+=1
pi=4*(nb_pts_interieurs/200000)
print(pi)

ecart=abs((math.pi-pi)/math.pi)*100

print(f'la valeur approximative de pi est : {pi}, le pourcentage d\'écart est de : {ecart}')