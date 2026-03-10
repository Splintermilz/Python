import random
import time

print("\v ❇️ Let's play to D&D !❇️")

# Variable de base :
hero_life = 100
enemy_life = 100
number_of_potion = 3
skip_turn = False
###############################################################################################################################################################

while True :
# Passement de tour du joueur :
    if skip_turn :
        print("🔴 Your skipe your turn...")
        skip_turn = False
    else : # Création d'une nouvelle VAR pour le CHOIX DU JOEUR - donc avec CDC vide
        user_choice = ""
        while user_choice not in ["1", "2", "3"] :
            user_choice = input("Would you like to attack (1), use a potion (2) or skip your turn (3) ? ")

# ATTACK DU HERO
        if user_choice == "1" : # Attack -
            your_attack = random.randint(10, 30)
            enemy_life -=  your_attack
            print("****************")
            print(f"Nice shot ! You inflict {your_attack} damage points! ⚔️")
            print("****************")
# ****************************   ***********************  **************************  **********************************
        elif user_choice == "2" : # Potion
            if number_of_potion > 0 :
                my_potion = random.randint(15 , 50)
                hero_life += my_potion
                number_of_potion  -= 1 # On enleve une potion du stock
                print("🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪")
                print(f"You take a potion. Your life increase for {my_potion}. 🧪")
                print("🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪")
                print(f"{number_of_potion} life potions left")
                if number_of_potion == 0 :
                    print("You don't have potion anymore ! Be carefull 🙇🏽‍♂️")

        elif user_choice == "3" : # Skip turn
            print("Your skip your turn, coward..")

# Indentation super importante pour la logique du code -
################## Creation du code pour le JEU DE L'ENNEMY ##################
# Code bancale = revoir la logique de toute la section - manque de "finesse"
    if user_choice in ["1", "2", "3"] :
        enemy_attack = random.randint(10, 30)
        hero_life -= enemy_attack
        print("⚡️*⚡️⚡️*⚡️⚡️*⚡️⚡️*⚡️")
        print(f"Enemy reply.. You have {hero_life} life points left")
        print("⚡️*⚡️⚡️*⚡️⚡️*⚡️⚡️*⚡️")

    elif enemy_life == 0 and hero_life ==0 :
            print("Your both died ! 👻 ")

    elif enemy_life == 0 :
            enemy_life -= your_attack
            print("🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆")
            print("Congratulation ! You win the D&D game ! 🏆")
            print("🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆")

    elif hero_life == 0 :
            print("🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚")
            print("You loose ! Maybe next time 👀")
            print("🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚🌚")
    break


