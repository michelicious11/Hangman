"""
Created on Fri Dec 27 08:57:25 2019

@authors: MP & SF & MM
"""

import mot as m

# variables globales
guesses = 0
counter_turn = 0
verity = False

#changer le nombre de guess
def set_guesses():
    global guesses
    while True:
        try:
            guesses = int(input("Choisissez le nombre d'essais : "))
            break
        except:
            print("That's not a valid option!")
    

#incrementer le tour de 1
def add_turn():
    global counter_turn
    global verity
    if guesses == counter_turn:
        print("\nDésolé, vous avez perdu!")
        print("\nLe mot à trouver était", m.word_to_find)
    elif guesses > counter_turn:
        m.pick_letter()
        check_letter()
        m.display_word()
        check_win_condition()
        if verity == True:
            print("\nFelicitations, vous avez gagne!")
        else :
            add_turn()

#pour savoir si c'est le premier tour
def check_first_turn():
    if counter_turn == 0:
        return True

# Verifier si on a gagne (2 conditions)
# verifier si il reste assez de tentatives (condition 1)
# et si les lettres de la liste picked_letters sont les memes que celui du word_to_find (condition 2)
# condition 1 : le nombre de tentatives doit etre > 0
# condition 2 : mettre les deux listes en ordre et les comparer
def check_win_condition():
    global counter_turn
    global guesses
    global verity

    f = set(m.list_of_picked_letters)
    t = set(m.word_to_find)

    g = f & t

    if len(g) == len(set(m.word_to_find)):
        verity = True
    else :
        verity = False

def check_letter():
    global guesses
    if m.lettre_choisie in m.word_to_find:
        print("\nCool!")
        print("\n", m.list_of_picked_letters)
        print("\n", m.list_of_available_letters)
        print("\nNumber of guesses: ", guesses)
    else:
        print("\nTry Again !")
        print("\n", m.list_of_picked_letters)
        print("\n", m.list_of_available_letters)
        guesses -= 1
        print("\nNumber of guesses: ", guesses)


def start_game():
    user_name = input("Quel est votre nom ? ")
    print("Bonjour ", user_name, ", nous allons commencer une partie de bonhomme pendu. \n", sep='')
    print("Le but du jeu est de trouver le mot cache. ")
    print("Essayez de deviner les lettres composant le mot dans le nombre de tentatives choisi.")
    set_guesses()
    print("Bonne chance!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    m.pick_random_word()
    m.display_word()
    add_turn()
