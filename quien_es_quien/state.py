import reflex as rx

from quien_es_quien.personaje_random import random_pj

class State(rx.State):

    personaje_jugador = random_pj()

    imagen_personaje = ""