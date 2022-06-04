#Fonction

import random

def genere_mdp():
    password = [] #Liste vide
    for i in range(nblettres):
        result = random.choice(list1) #Utilisation de la fonction random
        password.append(result) #Ajout de l'élément à la liste
        passwordstr = ''.join(str(x) for x in password) #Conversion de la liste en string
    result = print(passwordstr)
    return result




list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         '1','2','3','4','5','6','7','8','9','0',
         ]

print("Bienvenue dans le générateur de mot de passe !")

while True:
    try:
        global nblettres
        nblettres = int(input("Veuillez entrer le nombre de caractère que va comporter votre mot de passe :\n\n"))

        if nblettres >=1:
            break


        else:
            print("\nErreur, votre mot de passe doit contenir au moins une lettre, veuillez réessayer !\n\n")
    except TypeError:
        pass

genere_mdp()

input()
