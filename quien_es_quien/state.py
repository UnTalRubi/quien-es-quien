import reflex as rx
from quien_es_quien.logica.personaje_random import random_pj
from quien_es_quien.logica.caracteristicas import extraer_palabras_clave
from quien_es_quien.logica.devolver_nombres import comprobar_respuesta
from quien_es_quien.logica.evaluar_respuesta import correccion

class State(rx.State):

    personaje_jugador: str = "Jugador"
    mostrar_jugador: bool = False
    mostrar_resultado: bool = False

    personajes_incorrectos: list = []
    personajes_tumbados: list = []
    cantidad_tumbados: int = 0
    
    pregunta: str = ""
    palabras_clave: str = ""
    es_correcto: str = ""


    @rx.event
    def obtener_jugador(self):
        self.personaje_jugador = random_pj()


    def comprobacion(self):
        if self.cantidad_tumbados >= 23:
            self.mostrar_jugador= True
            return rx.toast.success(
                "Has ganado!", 
                description="El personaje correcto era " + self.personaje_jugador + ".", 
                position="top-center",
                style={
                    "border": "3px solid green",
                    "border-radius": "0.53m",
                }
            )
        elif self.es_correcto == "invalido":
            return rx.toast.warning("Prueba otra cosa!")
        elif self.es_correcto == "correcto":
            return rx.toast.success("Tiene la característica!")
        elif self.es_correcto == "incorrecto":
            return rx.toast.error("No tiene la característica!")


    @rx.event
    def obtener_caracteristicas(self):
        self.palabras_clave = extraer_palabras_clave(self.pregunta)

        self.personajes_incorrectos= comprobar_respuesta(self.palabras_clave,self.personaje_jugador)
        self.es_correcto = correccion(self.palabras_clave,self.personaje_jugador)
        self.personajes_tumbados.extend(self.personajes_incorrectos)
        self.personajes_tumbados= list(set(self.personajes_tumbados))
        self.cantidad_tumbados= len(self.personajes_tumbados)
        self.pregunta = ""
        self.palabras_clave = ""


    @rx.event
    def reiniciar_partida(self):
        self.mostrar_resultado = False
        self.mostrar_jugador = False
        self.pregunta = ""
        self.personajes_tumbados = []
        self.obtener_jugador()