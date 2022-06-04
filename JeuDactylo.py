"""
Programme Python permettant de s'améliorer en dactylographie avec le DactyloGame by Arthvr !

le principe est simple : un chaine de caractères composées de lettres et chiffres apparait à l'écran,
vous deviez la recopier le plus vite possible, et si possible sans erreur !

Arthvr 30/12/2021

Sources : 
https://www.it-swarm-fr.com/fr/python/mesurer-le-temps-ecoule-en-python/940039357/
https://www.it-swarm-fr.com/fr/python/afficher-un-flottant-avec-deux-decimales-dans-python/972896542/
https://openclassrooms.com/forum/sujet/identifier-la-difference-entre-deux-listes
"""

import time
import random

#LISTE DE TOUT LES ELEMENTS
list_clavier = [
    'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j',
    'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I',
    'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B',
    'N']

list_clavier_2 = [
    'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j',
    'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I',
    'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B',
    'N', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


#Fonction qui génère un str de façon aléatoire
def generator_word(): 
    word = []
    nb_lettres = random.randint(10,50) #Longueur de la str -> entre 10 et 20
    for i in range(nb_lettres):
        str1 = random.choice(list_clavier) #On prend au hasard 1 élément de list_clavier
        word.append(str1) #On l'ajoute à la liste word
        finalword = ''.join(str(x) for x in word) #Convertir la liste en str
    return finalword


#Fonction principale
def main():

    #PARTIE LANCEMENT DU JEU
    quest = generator_word() #str est égale à variable quest
    print(quest,"\n") #On affiche la str à recopier
    start = time.time() #On lance le chrono
    rep = str(input("Veuillez recopier ici : \n\n")) #Attend réponse utilisateur
    end = time.time() #Stoppe le chrono dès que l'utilisateur entre Enter
    time_user = end-start #Temps qu'à mit l'utilisateur à écrire
    print("\nVotre temps :",'%.2f' % time_user,"secondes\n") #Affiche time_user avec 2 décimales

    #PARTIE VERIFICATION
    nb_erreurs = 0 #Initialiser le nombre d'erreurs à 0
    quest_list = [] #Liste composée de tout les caract à recopier
    for element_quest in quest:
        quest_list.append(element_quest)

    rep_list = [] #Liste composée de tout les caract entrée par utilisateur
    for element_rep in rep:
        rep_list.append(element_rep)

    while len(rep_list) < len(quest_list): #Si l'utilisateur n'a pas rentré assez de caract
        space = " "
        rep_list.append(space) #Ajouter des str vides pour pouvoir zip() tout les caract

    if len(rep_list) > len(quest_list): #Si l'utilisateur a rentré trop de caract
        caract_en_trop = len(rep_list) - len(quest_list) 
        nb_erreurs += caract_en_trop #Rajouter à nbr erreurs le nbr de caract en trop

    list_zipped = list(zip(quest_list,rep_list)) #Crée une liste du type (quest1,rep1),...

    for element_zipped in list_zipped: #Parcoure tout les tuples de list_zipped
        if element_zipped[0] != element_zipped[1]: #Si caract 1 tuple est diff caract 2 tuple
            nb_erreurs += 1
            print(element_zipped,"Faute")
        else: #Si caract 1 tuple est égal caract 2 tuple
            print(element_zipped,"OK")
            continue
    
    if nb_erreurs ==0: #Si aucune erreur
        print("\nBien joué, vous n'avez fait aucune erreur !!!")
    else: #Si au moins 1 erreur
        print("\nVous avez commit ", nb_erreurs,"erreur(s)")

    nbr_bon_caract = len(rep_list) - nb_erreurs #Calcul du nombre de bon caract incrit

    moyenne_user= nbr_bon_caract / time_user #Calcul du nbr de bon caract divisé par temps
    moyenne_user_2 = float('%.2f' % moyenne_user) #Nbr de caract écrit par sec calculé en millième de sec
    calcul_mpm = moyenne_user_2 * 60 #Calcul nbr de caract écrit en minutes, conversion en min
    print("\nVotre vitesse de frappe est de",calcul_mpm,"caractères par minutes")

    taux_precision = nbr_bon_caract / len(rep_list) #Calcul taux de précision
    taux_precision_2 = taux_precision * 100 #Conversion en pourcents

    print("\nVotre taux de précision est de",'%.2f' % taux_precision_2,"%")

#PARTIE LANCEMENT FONCTIONS
main() #Lance la fonction main()

input() #Permet de garder la fenêtre Python ouverte lorsque le programme a fini

#Idée suite : afficher le nombre de lettres écrites à la minute mpm, vitesse de frappe, taux de précision %
#un classement du genre (si ,nbr lettres à la minute > 100: niveau TITAN)
