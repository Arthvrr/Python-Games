states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", 
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", 
    "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", 
    "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", 
    "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

founded = []


def find_state(liste):
    remaining_state = len(liste)
    found = 0

    while (remaining_state > 0):

        res = input("Donnez moi un état des USA : ")

        if res == "STOP":
            print(f"Vous avez trouvé un total de {found} états. Il en reste cependant {remaining_state}.\n")
            print("les états restants étaient : \n")
            for i in liste:
                print(i,"\n")
            break

        elif res in liste:
            liste.remove(res)
            founded.append(res)
            found += 1
            remaining_state -= 1
            print(f"Bravo ! Vous avez trouvé {found} états. Il en reste {remaining_state}.\n")
        
        else:
            if res in founded:
                print("Vous avez déjà trouvé cet état !\n")
            else:
                print("Ce n'est pas un état des USA\n")

find_state(states)
        

