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
    print("\nNombre d'essais : ", number_of_guesses)


def play_turn():
    show_number_of_guesses()
    mot.show_letters_picked()
    mot.check_word()
    if mot.found_letter:
        global number_of_remaining_letters
        number_of_remaining_letters -= 1
        print("NUMBER OF REMAINNN :::: ", number_of_remaining_letters)
    elif not mot.found_letter:
        lose_guess()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    end_game()
    

def start_game():
    user_name = input("Quel est votre nom ? ")
    print("Bonjour ", user_name, ", nous allons commencer une partie de bonhomme pendu. \n", sep='')
    print("Le but du jeu est de trouver le mot cache. ")
    print("Essayez de deviner les lettres composant le mot dans le nombre de tentatives choisi.")

    mot.pick_random_word()
    global number_of_remaining_letters
    number_of_remaining_letters = len(mot.word_to_find)
    global number_of_guesses
    number_of_guesses = 0 
    while True: 
      try: 
         number_of_guesses = int(input("Choisissez le nombre d'essais: ")) 
      except ValueError: 
         print("Veuillez entrer un nombre valide!") 
         continue
      else:
         print("Parfait!")
         break

    print("Bonne chance!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    mot.initiate_word()

def end_game():
    global number_of_guesses
    global number_of_remaining_letters
    if number_of_guesses == 0:
        print("Desole, vous avez perdu!")
        print("Le mot a trouver etait: ", mot.word_to_find)
    elif number_of_remaining_letters == 0:
        print("NUMBER OF REMAINNN :::: ", number_of_remaining_letters)
        print("Felicitations, vous avez gagne!")
    else:
        play_turn()


def play_hangman():
    start_game()
    play_turn()
