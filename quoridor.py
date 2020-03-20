import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description = "Jeu quoridor - Phase 1")
    parser.add_argument('-l', '--lister', action = 'store_true', help = 'Lister les identifiants de vos 20 dernières parties.')
    parser.add_argument('idul', metavar='idul', type = str, help = 'IDUL du joueur')
    # parser.add_argument('bar', type = str, help = 'Argument positionnel de la sous-commande acheter')
    return parser.parse_args()
