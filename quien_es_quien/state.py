import reflex as rx

from quien_es_quien.personaje_random import random_pj
from quien_es_quien.nombre_personaje import nombre_pj
class State(rx.State):

    personaje_jugador = random_pj()