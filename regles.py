"""
Created on Fri Dec 27 08:57:25 2019

@authors: MP & SF & MM
"""

import mot as m

# variables globales
counter_turn = 0
is_word_found = False

#changer le nombre de guess
# on a utilisé un try-except pour obliger l'utilisateur à introduire un integer
def set_guesses():
    while True:
        try:
            m.guesses = int(input("Choisissez le nombre d'essais : "))
            break
        except:
            print("Veuillez choisir un nombre!")
    

#incrementer le tour de 1
def add_turn():
    global counter_turn
    global is_word_found
    if m.guesses == counter_turn:
        print("\nDésolé, vous avez perdu!")
        print("\nLe mot à trouver était", m.word_to_find)
    elif m.guesses > counter_turn:
        m.pick_letter()
        m.check_letter()
        m.display_word()
        check_win_condition()
        if is_word_found == True:
            print("\nFelicitations, vous avez gagne!")
        else :
            add_turn()

# Verifier si on a gagne (2 conditions)
# verifier si il reste assez de tentatives (condition 1)
# et si les lettres de la liste picked_letters sont les memes que celui du word_to_find (condition 2)
# condition 1 : le nombre de tentatives doit etre > 0
# condition 2 : mettre les deux listes en ordre et les comparer

# La fonction check_win_condition transforme word_to_find et list_of_picked_letters en Sets
# On cree l'intersection entre les deux Sets pour extraire les lettres qui sont en commun
# ensuite on compare la longueur de l'intersection et du set word_to_find
# si c'est la longueur est la meme donc on a trouvé le mot, sinon on pas trouvé le mot.

def check_win_condition():
    global counter_turn
    global is_word_found #Boolean pour verifier la condition

    f = set(m.list_of_picked_letters)  # transformation de list_of_picked_letters en set
    t = set(m.word_to_find)  # transformation de word_to_find en set

    g = f & t # Intersection entre list_of_picked_letters et word_to_find

    if len(g) == len(set(m.word_to_find)): # condition : si la longueur de l'intersection et du set word_to_find est la même
        is_word_found = True  # changer la valeur pour vrai et donc on a trouvé le mot
    else:
        is_word_found = False  # changer la valeur pour faux et donc on a pas trouvé le mot

# fonction pour initialiser le debut de la partie avec les fonctions de regles
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
