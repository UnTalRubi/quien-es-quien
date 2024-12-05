import reflex as rx
from quien_es_quien.lista_personajes import personajes
from quien_es_quien.personaje_random import random_pj
from quien_es_quien.caracteristicas import extraer_palabras_clave
from quien_es_quien.devolver_nombres import devolver_nombre

class State(rx.State):

    personaje_jugador="Jugador"

    mostrar_jugador=False

    personaje_muerto="Alex"

    personajes_tumbados=[]
    pregunta=""
    respuesta=""
    extraer=[]
    obtener=[]

    @rx.event
    def obtener_jugador(self):
        self.personaje_jugador = random_pj(personajes)

    @rx.event
    def obtener_caracteristicas(self):
        self.extraer = extraer_palabras_clave(self.pregunta)
        self.obtener = devolver_nombre(self.respuesta)
        self.personajes_tumbados.append(self.obtener)
