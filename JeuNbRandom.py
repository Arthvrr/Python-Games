import random

nbrandom = random.randint(1,100)

#print(nbrandom) #Afficher le Nombre random

print('''

Jeu du nombre : vous devez trouver le nombre secret compris entre 1 et 100.

Vous avez 5 chances. Bonne chance !
''')

n = int(input("Veuillez entrer un nombre entre 1 et 100 : "))

nbchance = 1

while nbrandom != n and nbchance <5 and 1 <= n <=100:

    if nbrandom > n:
        print("Le nombre random est plus GRAND")
        nbchance += 1
        print("Il vous reste encore", 6-nbchance, "chances")
        n = int(input("Réessayer : "))

    elif nbrandom < n:
        print("le nombre random est plus PETIT")
        nbchance += 1
        print("Il vous reste encore", 6-nbchance, "chances")
        n = int(input("Réessayer : "))

if nbrandom == n:
    print("Vous avez gagné en", nbchance,"coup(s), bravo !")
    print("Le nombre random était :",nbrandom)

if nbchance == 5:
    print("Vous avez perdu, dommage !")
    print("Le nombre random était :",nbrandom)

input()#Pour garder fenêtre ouverte en fin de programme
