import reflex as rx
from quien_es_quien.lista_personajes import personajes
from quien_es_quien.personaje_random import random_pj

class State(rx.State):

    personaje_jugador="Jugador"

    @rx.event
    def obtener_jugador(self):
        self.personaje_jugador = random_pj(personajes)