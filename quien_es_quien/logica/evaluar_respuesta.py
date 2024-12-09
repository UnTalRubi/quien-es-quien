from quien_es_quien.variables.lista_personajes import PERSONAJES
from quien_es_quien.variables.lista_nombres import NOMBRES_PERSONAJES


def correccion(respuesta,jugador):
    posicion_jugador = NOMBRES_PERSONAJES.index(jugador)
    
    if not respuesta:
        return "invalido"
    elif respuesta not in PERSONAJES[posicion_jugador]:
        return "incorrecto"
    elif respuesta in PERSONAJES[posicion_jugador]:
        return "correcto"