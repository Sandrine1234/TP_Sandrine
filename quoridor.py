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

