import reflex as rx
from quien_es_quien.lista_personajes import personajes
from quien_es_quien.personaje_random import random_pj

class State(rx.State):

    personaje_jugador="Jugador"

    mostrar_jugador=False

    personaje_muerto="Alex"

    personajes_tumbados=["Alex","Alfred","Joe","Charles"]

    @rx.event
    def obtener_jugador(self):
        self.personaje_jugador = random_pj(personajes)

    @rx.event
    def tumbar_personajes(self):
        self.personajes_tumbados.append(self.personaje_muerto)