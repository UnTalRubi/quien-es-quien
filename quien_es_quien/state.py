import reflex as rx
from quien_es_quien.lista_personajes import personajes
from quien_es_quien.personaje_random import random_pj

class State(rx.State):

    personaje_jugador="Personaje"
    posicion=0
    imagen_personaje = "Alex.jpg"

    @rx.event
    def obtener_jugador(self):
        self.personaje_jugador = random_pj(personajes)

    @rx.event
    def obtener_personajes(self, posicion):
        self.imagen_personaje = personajes[posicion][0] + ".jpg"
        posicion += 1
        return str(self.imagen_personaje)
