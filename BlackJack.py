"""
BlackJack by Arthvr
"""
import random


AS = 1

list1 = [AS,2,3,4,5,6,7,8,9,10,10,10,10]
#As,2,3,4,5,6,7,8,9,10,Valet,Dame,Roi

somme = 0

somme_bot = 0

card1 = random.choice(list1)
card2 = random.choice(list1)

card1_bot = random.choice(list1)
card2_bot = random.choice(list1)

if card1 == AS or card2 == AS:
    x = int(input("AS ! Voulez vous prendre 1 ou 11 ?\n"))
    if x == 1:
        somme +=1
    elif x == 11:
        somme += 11
    

somme = card1+card2

somme_bot = card1_bot + card2_bot

print("Première Carte :",card1,"\n")
print("Seconde Carte :",card2,"\n")
print("Total =",somme,"\n")
#print("Total Adversaire =",somme_bot,"\n")

choix_bot = ['stay','card']

while True:

    if somme == 21: #SI USER = 21 -> WIN
        print("Vous avez gagné en ayant 21 ! Bien joué !")
        break

    elif somme_bot == 21: #SI BOT = 21 -> LOSE
        print("Votre adversaire a gagné en ayant 21")
        break
    
    elif somme_bot < 22 and somme < 22: #SI AUCUN DES DEUX N'A ENCORE PERDU
        choix = input("Voulez vous reprendre une carte (card) ou se coucher ? (stay) ")
        
        if choix == 'card': #SI USER DECIDE PRENDRE CARTE
            card3 = random.choice(list1)
            somme += card3
            choix_final_bot = random.choice(choix_bot)
            
            if choix_final_bot == 'card':
                print("\nVotre adversaire a décidé de prendre une carte")
                card3_bot = random.choice(list1)
                somme_bot += card3_bot

            elif choix_final_bot == 'stay':
                print("\nVotre adversaire a décidé de se coucher")

            print("\nTotal =",somme,"\n")
            print("\nTotal Adversaire =",somme_bot,"\n")

        if choix == 'stay': #SI USER DECIDE DE SE COUCHER
            choix_final_bot = random.choice(choix_bot)
            
            if choix_final_bot == 'card':
                print("\nVotre adversaire a décidé de prendre une carte")
                card3_bot = random.choice(list1)
                somme_bot += card3_bot

            elif choix_final_bot == 'stay':
                print("\nVotre adversaire a décidé de se coucher")

            print("\nTotal =",somme,"\n")
            print("\nTotal Adversaire =",somme_bot,"\n")

            if somme_bot > somme and somme_bot < 22:
                print("\nVotre adversaire a gagné")
            elif somme_bot < somme and somme < 22:
                print("\nVous avez gagné !")

            break

    elif somme_bot > 21 and somme < 22: #BOT A PERDU -> WIN
        print("\nVous avez gagné ! Votre adversaire a perdu en ayant plus de 21\n")
        break

    elif somme_bot < 22 and somme > 21: #USER A PERDU -> LOSE
        print("\nVous avez perdu. Vous avez obtenu plus de 21\n")
        break

    elif somme_bot < 22 and somme > 22: #USER & BOT ONT PERDU -> LOSE
        print("\n Vous et votre adversaire ont tout les deux perdu en ayant plus que 21\n")
        break

input()






    
