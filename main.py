# Créé en septembre 2023 par Alexandre Wilbur
# choisi un chiffre au hasard entre des valeurs définies par l'utilisateur et lui demande de le deviner
from random import *


# déclaration de la fonction qui vérifiera l'essai

def deviner(inconnu):
    essai = -1
    nmbessais = 0
    while essai != inconnu:
        essai = int(input("Entrez un chiffre entre les deux bornes:"))
        nmbessais = nmbessais + 1
        if essai > inconnu:
            print("Votre nombre est plus grand que l'inconnu\n")
        elif essai < inconnu:
            print("Votre nombre est plus petit que l'inconnu\n")
        elif essai == inconnu:
            print("Bravo! Votre score est : ", nmbessais, "\n")


# Demande pour recommancer le jeu
retry = "Oui"
while retry == "Oui":
    a = int(input("C'est quoi la borne minimale?"))
    b = int(input("C'est quoi le borne maximale?"))
    input_inconnu = randint(a, b)
    deviner(input_inconnu)
    retry = str(input("Voulez-vous rejouer? (Oui ou Non)"))
