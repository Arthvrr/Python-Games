#Jeu Pierre-Papier-Ciseaux ou CHIFOUMI

import random

while True:
    try:
        choixUser = str(input("Jeu du Pierre Papier Ciseaux ! Veuillez choisir entre Pierre, Papier ou Ciseaux : \n\n--> "))
        poss = ["Pierre","Papier","Ciseaux"]
        choixPNJ = random.choice(poss)

            
        if choixUser == 'Pierre': #Si utilisateur choisit PIERRE
            if choixPNJ =='Papier':
                print("\n",choixUser,"perd face à",choixPNJ,"l'ordinateur remporte la manche !\n")
            elif choixPNJ == 'Ciseaux':
                print("\n",choixUser,"bat",choixPNJ,"l'utilisateur remporte la manche !\n")
            elif choixPNJ == 'Pierre':
                print("\nÉgalité ! Vous avez tout les deux choisi",choixPNJ,"\n")
                
        elif choixUser == 'Papier': #Si utilisateur choisit PAPIER
            if choixPNJ =='Pierre':
                print("\n",choixUser,"bat",choixPNJ,"l'utilisateur remporte la manche !\n")
            elif choixPNJ == 'Ciseaux':
                print("\n",choixUser,"perd face à",choixPNJ,"l'ordinateur remporte la manche !\n")
            elif choixPNJ == 'Papier':
                print("\nÉgalité ! Vous avez tout les deux choisi",choixPNJ,"\n")

        elif choixUser == 'Ciseaux': #Si utilisateur choisit CISEAUX
            if choixPNJ =='Papier':
                print("\n",choixUser,"bat",choixPNJ,"l'utilisateur remporte la manche !\n")
            elif choixPNJ == 'Pierre':
                print("\n",choixUser,"perd face à",choixPNJ,"l'ordinateur remporte la manche !\n")
            elif choixPNJ == 'Ciseaux':
                print("\nÉgalité ! Vous avez tout les deux choisi",choixPNJ,"\n")
        else:
            print("\nCommande invalide, veuillez choisir entre PIERRE PAPIER ou CISEAUX\n")        
    except:
        pass

