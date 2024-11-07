import random
import time

def slot():
    with open("save.txt",'r',encoding="utf-8") as file:
        txt = file.read()
        solde = txt[:]
        print(solde)
    mise = int(input("\nPlacer ici votre mise : "))
    calcul = int(solde) - mise #On regarde si la mise est possible ou non
    if calcul < 0:
        print("\nPas assez de fonds, veuillez réessayer !\n")
    else:
        solde = calcul
        print("\nVotre mise est de",mise,"et votre solde est de",solde,"\n")
        print("\nMachine lancée !\n")
        time.sleep(2)
        #PARTIE LANCEMENT SLOT
        temps_donné = random.randint(100000,500000)
        list_elements = ["$","£","€"]
        choix1 = random.choice(list_elements)
        choix2 = random.choice(list_elements)
        choix3 = random.choice(list_elements)
        resultat = [choix1,choix2,choix3]
        temps = 0
        while temps < temps_donné:
            list_elements = ["$","£","€"]
            choix1 = random.choice(list_elements)
            choix2 = random.choice(list_elements)
            choix3 = random.choice(list_elements)
            resultat = [choix1,choix2,choix3]
            print(resultat)
            temps += 1
        while temps == temps_donné:
            resultat_final = []
            for i in resultat:
                resultat_final.append(i)
            print("RESULTAT",resultat_final)
            break

            #PARTIE VERIF SLOT
        nb_elements_différents = 0
        unique_list = [] #Liste représentants tout les éléments diff de resultat
        for i in resultat_final:
            if i not in unique_list:
                unique_list.append(i)
                nb_elements_différents += 1
            else:
                continue

        if nb_elements_différents == 1:
            print("\nJACKPOT !!! MISE X10 !!!\n")
            calcul = mise * 10
            solde = solde + calcul
            print("\nVotre solde s'élève à",int(solde),"\n")

        elif nb_elements_différents == 2:
            calcul = mise * 1.25
            solde = solde + calcul
            print("\nBien Joué ! MISE X1.25 !")
            print("\nVotre solde s'élève à",int(solde),"\n")
        else:
            solde = solde
            print("\nZut... Mise perdue...\n")
            print("\nVotre solde s'élève à",int(solde),"\n")

        if solde <= 0:
            print("\nPerdu... relance une partie !")
    
    with open("save.txt","w",encoding="utf-8") as file:
        file.write(str(int(solde)))
    


while True:
    slot()

input()
