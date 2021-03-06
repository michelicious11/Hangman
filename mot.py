"""
Created on Fri Dec 27 09:11:37 2019

@authors: MP & SF & MM
"""

import random
import xlrd
import string
import re
#import regles as r

# variables
loc = "WordDB50.xlsx"
word_to_find = None
list_of_available_letters = list(string.ascii_lowercase)
list_of_picked_letters = []
letter_turn = ""
guesses = None


# 1ere etape avoir un mot cache
# fonction pour selectionner un mot au hasard dans le fichier excel
def pick_random_word():
    global word_to_find
    workbook = xlrd.open_workbook(loc)
    worksheet = workbook.sheet_by_index(0)
    word_to_find = str(worksheet.cell(random.randint(1, 50), 0).value)
    word_to_find = word_to_find.lower()

    print("\nThe Word:", word_to_find)

# 2e etape, afficher le mot cache
# fonction pour imprimer les tirets pour chaque lettre
def display_word():
    for letter in word_to_find:
        if letter not in list_of_picked_letters:
            print("-", end='')
        else:
            print(letter, end='') #Added this pour print les bonne lettres


# 3e etape, le joueur choisit une lettre
# fonction pour choisir une lettre - ajoute lettre dans liste lettres choisi et la retire de liste lettre non choisies
# si lettre deja choisie, message avisant le joueur
def pick_letter():
    global lettre_choisie
    is_invalid_letter = True
    while is_invalid_letter:
        lettre_choisie = input("\nChoisissez une lettre : ").lower()
        if not re.match("^[a-z]*$", lettre_choisie):
            print("Vous devez choisir une lettre!")
        else:
            if lettre_choisie in list_of_available_letters:
                list_of_available_letters.remove(lettre_choisie)
                list_of_picked_letters.append(lettre_choisie)
                is_invalid_letter = False
            else:
                print("La lettre a deja ete choisie!")
    return lettre_choisie

# La fonction check_letter va verifier si la lettre choisie est bonne ou mauvaise
# Et changer le nombre d'essai dépendamment de la lettre choisie.
def check_letter():
    global guesses
    if lettre_choisie in word_to_find:
        print("\n", list_of_picked_letters)
        print("\n", list_of_available_letters)
    else:
        print("\n", list_of_picked_letters)
        print("\n", list_of_available_letters)
        guesses -= 1 # la decrementation ce passe ici
    print("\nNombre d'essais: ", guesses)