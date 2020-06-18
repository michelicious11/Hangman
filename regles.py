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
# on a utilisé un try-except pour obliger l'utilisateur à introduire un integer
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

#La fonction check_win_condition va transformer word_to_find et list_of_picked_letters en Sets 
#Un Set (c'est comme une liste en forme de dictionnaire) Google it god damnit !!
#puis va faire l'intersection entre les deux Sets pour extraire les lettres qui sont en commun
#ensuite on compare la longueur de l'intersection et du set word_to_find
#si c'est la longueur donc on a trouvé le mot, sinon on pas trouvé le mot.

def check_win_condition():
    global counter_turn
    global guesses
    global verity #Boolean pour verifier la condition

    f = set(m.list_of_picked_letters) # transformation de list_of_picked_letters en set
    t = set(m.word_to_find) # transformation de word_to_find en set

    g = f & t #Intersection entre list_of_picked_letters et word_to_find

    if len(g) == len(set(m.word_to_find)): # condition : si la longueur de l'intersection et du set word_to_find est la même
        verity = True #retourne vrai et donc on a trouvé le mot
    else :
        verity = False #retourne faux et donc on a pas trouvé le mot

#La fonction check_letter va verifier si la lettre choisie est bonne ou mauvaise
#Et changer le nombre d'essai dépendamment de la lettre choisie.
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
        guesses -= 1 # la decrementation ce passe ici
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
