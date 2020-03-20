import json
import requests


def lister_parties(idul):
    url_lister = 'https://python.gel.ulaval.ca/quoridor/api/lister/'
    try:
        parametre = requests.get(url_lister, params={'idul': idul})
        if parametre.status_code == 200:
            parametre = parametre.text
            json_x = json.loads(donnees)
            json_y = json.dumps(json_x, indent=2)
            print(json_y)
        else:
            print("Le GET sur '{}' a produit le code d'erreur {}".format(url_lister, parametre.status_code))
    except RuntimeError as error:
        print(error)
