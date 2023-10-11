# Créé en septembre 2023 par Alexandre Wilbur
# choisi un chiffre au hasard entre des valeurs définies par l'utilisateur et lui demande de le deviner

from random import*

# déclaration de la fonction qui vérifiera l'essai
def deviner(inconnu):
    essai = -1
    nmbessais = 0
    while essai != inconnu:
        essai = int(input("Entrez un chiffre entre les deux bornes:"))
        if essai > inconnu:
            nmbessais = nmbessais + 1
            print("Votre nombre est plus grand que l'inconnu\n")
        elif essai < inconnu:
            nmbessais = nmbessais + 1
            print("Votre nombre est plus petit que l'inconnu\n")
        elif essai == inconnu:
            nmbessais = nmbessais + 1
            print("Bravo! Votre score est : ", nmbessais, "\n")

deviner(randint(int(input("C'est quoi la borne minimale?")), int(input("C'est quoi le borne maximale?"))))
#Demande pour recommancer le jeu
retry = "Oui"
while retry == "Oui":
    retry = str(input("Voulez-vous rejouer? (Oui ou Non)"))
    if retry == "Oui": deviner(randint(int(input("C'est quoi la borne minimale?")), int(input("C'est quoi le borne maximale?"))))