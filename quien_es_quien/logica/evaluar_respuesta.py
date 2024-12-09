from quien_es_quien.variables.lista_personajes import personajes
from quien_es_quien.variables.lista_nombres import nombres_personajes


def correccion(respuesta,jugador):
    posicion_jugador = nombres_personajes.index(jugador)
    
    if not respuesta:
        return "invalido"
    elif respuesta not in personajes[posicion_jugador]:
        return "incorrecto"
    elif respuesta in personajes[posicion_jugador]:
        return "correcto"