import random
from quien_es_quien.lista_personajes import personajes

def random_pj():
    return ((random.choice(personajes))[0])

print (random_pj)