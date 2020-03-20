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
        
 def initialiser_partie(idul):
    url_debut = 'https://python.gel.ulaval.ca/quoridor/api/initialiser/'
    try:
        parametre = requests.post(url_debut, data={'idul': idul})
        if parametre.status_code == 200:
            json_parametre = parametre.json()
            return json_parametre['id'], json_parametre['état']
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}".format(
                url_debut, parametre.status_code
            ))
    except RuntimeError as error:
        print(error)

 def jouer_coup(id_partie, type_coup, position):
    url_coup = 'https://python.gel.ulaval.ca/quoridor/api/jouer/'
    try:
        parametre = requests.post(url_coup, data={'id': id_partie,
        'type': type_coup, 'pos': position})
        if parametre.status_code == 200:
            json_parametre = parametre.json()
            if 'gagnant' in json_parametre:
                raise StopIteration(json_parametre['gagnant'])
            elif 'message' in json_parametre:
                print(json_parametre['message'])
            else:
                return json_parametre
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}.".format(
                url_coup, parametre.status_code
            ))
    except RuntimeError as error:
        print(error)
