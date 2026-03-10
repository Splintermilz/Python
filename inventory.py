import sys

liste = []

print("\vBienvenue dans votre application de Liste !")# \v : tabulation verticale - sans espace
print("Choisissez parmi les 5 options suivantes :")

while True :
    print("\v1: Ajouter un élément à la liste") # \v : tabulation verticale - sans espace
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")

    main_request = input("Votre choix : ") # Pas besoin de str() car input() renvoie déjà une str

    if main_request == '1': # Compare avec des chaînes maintenant
        element_to_add = input("Quel élément voulez-vous ajouter ? ") #Variable combinée avec Input pour ajout de l'Item
        liste.append(element_to_add)
        print(f"Votre liste est bien mise à jour ! Elle contient maintenant l'item suivant : {liste} ")


    elif main_request == '2': # Creation d'une deuxieme var pour deuxieme element
        element_to_add2 = input("Quel élément voulez-vous retirer ?")
        liste.remove(element_to_add2)
        print(f"Votre liste est bien mise à jour ! L'item suivant a bien été retiré : {liste} ")

    elif main_request == '3':
        print(f"Voici votre liste : {liste}.")

    elif main_request == '4':
        liste.clear()
        print("Votre liste est vide.")

    elif main_request == '5':
        print("Au revoir !")
        sys.exit() # permet de quitter le programme grâce au module sys

    else: # Permet de revenir sur l'option choix
        print("Veuillez choisir parmi les 5 options proposées !")
        input("Votre choix :")

