import reflex as rx
from quien_es_quien.personaje_random import random_pj
from quien_es_quien.caracteristicas import extraer_palabras_clave
from quien_es_quien.devolver_nombres import comprobar_respuesta

class State(rx.State):

    personaje_jugador: str = "Jugador"
    mostrar_jugador: bool = False

    personajes_incorrectos: list = []
    personajes_tumbados: list = []
    
    pregunta: str = ""
    extraer: str = ""


    @rx.event
    def obtener_jugador(self):
        self.personaje_jugador = random_pj()


    @rx.event
    def obtener_caracteristicas(self):
        self.extraer = extraer_palabras_clave(self.pregunta)
        self.personajes_incorrectos = comprobar_respuesta(self.extraer,self.personaje_jugador)
        self.personajes_tumbados.extend(self.personajes_incorrectos)
        self.pregunta = ""


    @rx.event
    def reiniciar_partida(self):
        self.pregunta = ""
        self.personajes_tumbados = []
        self.obtener_jugador()