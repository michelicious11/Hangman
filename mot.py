# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 09:11:37 2019

@authors: MP & SF & MM
"""

import random
import xlrd
import string
import re

# variables
loc = "WordDB50.xlsx"
word_to_find = None
list_of_available_letters = list(string.ascii_lowercase)
list_of_picked_letters = []
letter_turn = ""

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
    global word_to_find
    for letter in word_to_find:
        if letter not in list_of_picked_letters:
            print("-", end='')


# 3e etape, le joueur choisit une lettre
# fonction pour choisir une lettre - ajoute lettre dans liste lettres choisi et la retire de liste lettre non choisies
# si lettre deja choisie, message avisant le joueur
def pick_letter():
    is_invalid_letter = True
    while is_invalid_letter:
        lettre_choisie = input("Choisissez une lettre : ").lower()
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