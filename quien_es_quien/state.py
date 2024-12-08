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
    palabras_clave: str = ""
    es_correcto: str = ""


    @rx.event
    def obtener_jugador(self):
        self.personaje_jugador = random_pj()


    @rx.event
    def obtener_caracteristicas(self):
        self.palabras_clave = extraer_palabras_clave(self.pregunta)
        self.personajes_incorrectos, self.es_correcto= comprobar_respuesta(self.palabras_clave,self.personaje_jugador)
        self.personajes_tumbados.extend(self.personajes_incorrectos)
        self.pregunta = ""
        self.palabras_clave = ""


    @rx.event
    def comprobacion(self):
        if self.es_correcto == "invalido":
            return rx.toast.warning("Prueba otra cosa!")
        if self.es_correcto == "correcto":
            return rx.toast.success("Tiene la característica!")
        if self.es_correcto == "incorrecto":
            return rx.toast.error("No tiene la característica!")



    @rx.event
    def reiniciar_partida(self):
        self.pregunta = ""
        self.personajes_tumbados = []
        self.obtener_jugador()