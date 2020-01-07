# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 09:11:37 2019

@author: Mick Pl
"""

import random
import xlrd
import string

# variables
loc = "WordDB50.xlsx"
word_to_find = None
picked_letter = None
list_of_available_letters = list(string.ascii_lowercase)
list_of_picked_letters = []
found_letter = False


# fonction pour selectionner un mot au hasard dans le fichier excel
def pick_random_word():
    global word_to_find
    workbook = xlrd.open_workbook(loc)
    worksheet = workbook.sheet_by_index(0)
    word_to_find = str(worksheet.cell(random.randint(1, 50), 0).value)
    word_to_find = word_to_find.lower()


# fonction pour choisir une lettre - ajoute lettre dans liste lettres choisi et la retire de liste lettre non choisies
# si lettre deja choisie, message avisant le joueur
def pick_letter():
    global picked_letter
    is_letter_picked = True
    while is_letter_picked:
        picked_letter = input("\nPick a letter: ")
        picked_letter = picked_letter.lower()
        if picked_letter in list_of_available_letters:
            list_of_available_letters.remove(picked_letter)
            list_of_picked_letters.append(picked_letter)
            is_letter_picked = False
        else:
            print("La lettre a deja ete choisie!")


def initiate_word():
    global word_to_find
    for letter in word_to_find:
        if letter in list_of_picked_letters:
            print(letter, end='')
        elif letter not in list_of_picked_letters:
            print("-", end='')


# fonction pour imprimer le mot avec les bonnes lettres choisies
def check_word():
    global word_to_find
    global found_letter
    found_letter = False
    pick_letter()
    for letter in word_to_find:
        if letter in list_of_picked_letters:
            print(letter, end='')
            found_letter = True
        elif letter not in list_of_picked_letters:
            print("-", end='')



def show_letters_picked():
    global list_of_picked_letters
    print("Lettres choisies : ", end='')
    if not list_of_picked_letters:
        print("aucune")
    else:
        for letter in list_of_picked_letters:
            print(letter, end=' ')
