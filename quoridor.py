import argparse


# définition de la première fonction analyser commande
def analyser_commande():
    # module parser est un module qui fournit une interface à l'analyseur interne de Python
    parser = argparse.ArgumentParser(description = "Jeu quoridor - Phase 1")
    parser.add_argument('-l', '--lister', action = 'store_true', help = 'Lister les identifiants de vos 20 dernières parties.')
    parser.add_argument('idul', metavar='idul', type = str, help = 'IDUL du joueur')
    # parser.add_argument('bar', type = str, help = 'Argument positionnel de la sous-commande acheter')
    return parser.parse_args()

# pour la deuxième fonction
def line_namer(i):
    b = []
    if (((i + 1) // 2) + 1) < 10:
        b = ["{} |".format(((i + 1) // 2) + 1)]
    # si respecte pas la première condition
    else:
        b = ["{}|".format(((i + 1) // 2) + 1)]
    # retourne une liste
    return b

def afficher_damier_ascii(grille):
    grille = {"joueurs": [{"nom": "idul", "murs":7, "pos": [5, 5]},
    {"nom":"automate", "murs":3, "pos": [8, 6]}
    ],
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7,8]],
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7,7]]
        }
    }

    position_tableau = 9
    espace_horiz = ((position_tableau * 4) - 1)
    # tableaux d'équivalences entre les adresses du jeu et notre tableau
    posx_jeu = range(1, (position_tableau * 4), 4)
    posy_jeu = range(((position_tableau -1 ) * 2), -1, -2)
    # Le tableau de jeu est crée
    # place holder ou on ajoute tous les joueurs (pas plus que 2 joueurs)
    legende = "legende: "
    tableau = [legende]
    # tableau de jeu
    for i in reversed(range((position_tableau * 2) - 1)):
        if (i % 2) == 0:
            tableau += line_namer(i)
            tableau += [' ', '.']
            tableau += ([' ', ' ', ' ', '.'] * (position_tableau - 1))
            tableau += [' ', '|\n']
        else:
            tableau += ["  |"]
            tableau += ([' '] * espace_horiz)
            tableau += ['|\n']
    tableau += "--|" + ('-' * espace_horiz) +'\n'
    tableau += (' ' * 2) + '| '
    for i in range (1, position_tableau):
        tableau += str(i) + (' ' * 3)
    tableau += "{}\n".format(position_tableau)
    for num, joueur in enumerate(grille["joueurs"]):
        #pour mettre nom du joueur à la legende du tableau
        legende += "{}={} ".format((num +1), joueur['nom du joueur'])
        # position [x, y] du joueur en question
        position = joueur["posi"]
        # vérif position joueur
        if ((0 > position[0] > position_tableau)or
                (0 > position[1] > position_tableau)):
            raise IndexError ("Adresse du joueur invalide!")
    # décallage relatif
    indice = (posx_jeu[(position[0]-1)]+
              (posy_jeu[(position[1] - 1)] * espace_horiz))
    decallage= ((((indice + 1) // espace_horiz) * 2)+2)
    indice += decallage
    # insérer personnage dans tableau
    tableau[indice] = str(num + 1)
    # compléter legende tableau
    tableau[0] = legende + '\n' + (' ' * 3) + ('-' * espace_horiz) + '\n'
    #mur horiz
    for murhoriz in grille["murs"]["horizontaux"]:
        if ((1 > murhoriz[0] > (position_tableau -1)) or
                (2 > murhoriz[1] > position_tableau)):
            raise IndexError("Position du mur horizontal invalide!")
        indice = ((posx_jeu[(murhoriz[0] - 1)] -1) +
                   ((posy_jeu[(murhoriz[1] - 1)] + 1) * espace_horiz))
        decallage = ((((indice + 1) // espace_horiz) * 2) + 2)
        indice += decallage
        # itération pour les 5 murs
        for i in range(7):
            tableau [(indice + i)] = '-'
    # mur verticaux
    for murverti in grille ["murs"]["verticaux"]:
        if (2 > murverti[0] > position_tableau) or (1 > murverti[1] > position_tableau):
            raise IndexError("Position du mur vertical invalide!")
        indice = ((posx_jeu[(murverti[0] - 1)] - 2) +
                   ((posy_jeu[murverti[1] - 1]) * espace_horiz))
        decallage = ((((indice + 1) // espace_horiz) * 2) + 2)
        indice += decallage
        # itérer pour placer 3 murs
        for i in range(3):
            tableau[(indice - (i * (espace_horiz + 2)))] = '|'
    # afficher jeu sous forme d'une chaine de caractère
    print(''.join(tableau))
