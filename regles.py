# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:57:25 2019

@authors: MP & SF & MM
"""

import mot as m

# variables globales
guesses = 0
counter_turn = 0

#changer le nombre de guess
def set_guesses():
    global guesses
    guesses = int(input("Choisissez le nombre d'essais : "))

#incrementer le tour de 1
def add_turn():
    global counter_turn
    counter_turn += 1

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
    print("\ncounter = ", counter_turn, " - guesses = ", guesses, " - last = ", (len(m.word_to_find) - 1))
    print(m.list_of_picked_letters)
    if guesses > 0:
        m.letter_turn = m.pick_letter()
        if m.letter_turn in m.word_to_find:
            if check_first_turn():
                add_turn()
                check_win_condition()
            else:
                for letter in m.word_to_find:
                    index = list(m.word_to_find).index(letter)
                    if letter in m.list_of_picked_letters and index == list(m.word_to_find)[(len(m.word_to_find) - 1)]:
                        print("Felicitations, vous avez gagne!")
                    else:
                        add_turn()
                        print("cool")
        else:
            add_turn()
            guesses -= 1
            print("why?")
            print(guesses)
            check_win_condition()
    else:
        print("Desole, vous avez perdu!")
        print("Le mot a trouver etait", m.word_to_find)

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
    check_win_condition()


"""
def lose_guess():
    global number_of_guesses
    number_of_guesses -= 1


def show_number_of_guesses():
    global number_of_guesses

    print("\nNombre d'essais : ", number_of_guesses)
    print("Nombre d'essais : ", number_of_guesses)


def play_turn():
    show_number_of_guesses()
    mot.show_letters_picked()
    mot.check_word()
    mot.print_word()
    number_of_remaining_letters = len(mot.word_to_find)
    if mot.found_letter:
        number_of_remaining_letters -= 1
    elif not mot.found_letter:
        lose_guess()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    end_game()


def end_game():
    global number_of_guesses
    global number_of_remaining_letters
    if number_of_guesses == 0:

    elif number_of_remaining_letters == 0:
  
    else:
        play_turn()


def play_hangman():
    start_game()
    play_turn()
    
    **

"""