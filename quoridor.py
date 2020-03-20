import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description = "Jeu quoridor - Phase 1")
    parser.add_argument('-l', '--lister', action = 'store_true', help = 'Lister les identifiants de vos 20 dernières parties.')
    parser.add_argument('idul', metavar='idul', type = str, help = 'IDUL du joueur')
    # parser.add_argument('bar', type = str, help = 'Argument positionnel de la sous-commande acheter')
    return parser.parse_args()

def line_namer(i):
    b = []
    if (((i + 1) // 2) + 1) < 10:
        b = ["{} |".format(((i + 1) // 2) + 1)]
    else:
        b = ["{}|".format(((i + 1) // 2) + 1)]
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
