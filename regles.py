# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:57:25 2019

@author: Mick Pl
"""

import mot

# variables
number_of_guesses = None
number_of_remaining_letters = None


def lose_guess():
    global number_of_guesses
    number_of_guesses -= 1


def show_number_of_guesses():
    global number_of_guesses
    print("Nombre d'essais : ", number_of_guesses)


def play_turn():
    show_number_of_guesses()
    mot.show_letters_picked()
    mot.check_word()
    mot.pick_letter()
    lose_guess()
    mot.check_word()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    end_game()


def start_game():
    user_name = input("Quel est votre nom ? ")
    print("Bonjour", user_name, ", nous allons commencer une partie de bonhomme pendu. \n")
    print("Le but du jeu est de trouver le mot cache. ")
    print("Essayez de deviner les lettres composant le mot dans le nombre de tentatives choisi.")

    mot.pick_random_word()
    global number_of_remaining_letters
    number_of_remaining_letters = len(mot.word_to_find)
    global number_of_guesses
    number_of_guesses = int(input("Choisissez le nombre d'essais : "))
    print("Bonne chance!")
    print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def end_game():
    global number_of_guesses
    global number_of_remaining_letters
    if number_of_guesses == 0:
        print("Desole, vous avez perdu!")
    elif number_of_remaining_letters == 0:
        print("Felicitations, vous avez gagne!")
    else:
        play_turn()


def play_hangman():
    start_game()
    play_turn()