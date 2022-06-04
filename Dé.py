import random

dé = input('Jeu du dé chakal, appyez sur d pour lancer le dé\n\n')

while True:
    
    try:    
        if dé == 'd': #SI UTILISATEUR TAPE SUR D
            result = random.randint(1,6)
            print(result)

            dé = input('\nRelance le dé avec d\n\n')

        elif dé == '*': #METHODE POUR TRICHER
            cheat = int(input(''))
            if cheat >=1 and cheat <=6:
                dé = input('\nRelance le dé avec d\n\n')
                if dé == 'd':
                    result = cheat
                    print(result)
                
                dé = input('\nRelance le dé avec d\n\n')
        
        else:
            print("\nAppuie sur 'd' pour lancer le dé !\n\n")

            dé = input('\nRelance le dé avec d\n\n')


    except:
        pass

input()

